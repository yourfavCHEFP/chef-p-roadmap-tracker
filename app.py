"""
CHEF_P Roadmap Tracker — Streamlit app
Machine Learning -> MLOps -> AI Engineer -> Polish & Interview Prep
65 weeks starting Oct 1, 2026.
"""
import base64
import io
import json
import os
import re
import urllib.parse
import zipfile
from datetime import date, datetime, timedelta

import requests
import streamlit as st
import graphviz

from roadmap_content import STATIC_CONTENT, TOPIC_ILLUSTRATIONS
from resources_data import WEEK_RESOURCES
from assignments_data import ASSIGNMENTS

# ----------------------------------------------------------------------
# PERSISTENCE BACKEND
# Supabase if secrets are configured (survives Streamlit Cloud restarts
# and redeploys); falls back to a local JSON file otherwise (fine for
# local testing, but NOT durable on Streamlit Cloud).
# ----------------------------------------------------------------------
def _get_secret(key):
    try:
        return st.secrets[key]
    except Exception:
        return None


SUPABASE_URL = _get_secret("SUPABASE_URL")
SUPABASE_KEY = _get_secret("SUPABASE_KEY")
USE_SUPABASE = bool(SUPABASE_URL and SUPABASE_KEY)

if USE_SUPABASE:
    from supabase import create_client

    _supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    _ROW_ID = "chefp"

# ----------------------------------------------------------------------
# LEARN WITH AI ("Quick Explain" / "Teach Me" / "Quiz Me")
# Hand-written content in roadmap_content.py — zero API cost, zero API
# key, zero setup. Keyed by each week's topic name (see CURRICULUM below).
# A concept/sub-topic click reuses its parent week's content, since that's
# the level this content is written at.
# ----------------------------------------------------------------------
AI_LABELS = {"explain": "Quick Explain", "teach": "Teach Me", "quiz": "Quiz Me"}


def get_static_content(mode, item):
    entry = STATIC_CONTENT.get(item)
    if not entry:
        return f"_No written lesson yet for '{item}'._"
    return entry[mode]


def _md_inline_to_html(text):
    """Convert the two inline markdown patterns our lesson text actually
    uses (code spans, bold) to HTML, since raw HTML passed to st.markdown
    doesn't get its *contents* re-parsed as markdown."""
    text = re.sub(r'`([^`]+)`', r'<code style="background:#f1f1f1;padding:1px 5px;'
                                 r'border-radius:4px;font-size:.88em">\1</code>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    return text


TEACH_SECTION_STYLE = {
    "What it is": ("💡", "#eff6ff", "#3b82f6"),
    "Why it matters": ("🎯", "#f0fdf4", "#1e9e5a"),
    "How it works": ("⚙️", "#f5f3ff", "#7c3aed"),
    "Common mistake": ("⚠️", "#fffbeb", "#d97706"),
}


def render_teach_lesson(week_focus, text):
    """Renders a Teach Me lesson as glossy colored cards per section, with
    a hand-illustrated diagram on top when one exists for this topic."""
    illo = TOPIC_ILLUSTRATIONS.get(week_focus)
    if illo:
        st.iframe(illo, height=180, width="content")

    parts = re.split(r'\*\*(What it is|Why it matters|How it works|Common mistake)\*\*', text)
    it = iter(parts[1:])
    for header in it:
        body = next(it, "").strip(" \n")
        icon, bg, border = TEACH_SECTION_STYLE.get(header, ("📘", "#f9f9f9", "#999"))
        st.markdown(
            f"<div style='background:{bg};border-left:4px solid {border};border-radius:9px;"
            f"padding:11px 15px;margin-bottom:9px;box-shadow:1px 2px 4px #0001'>"
            f"<div style='font-weight:700;margin-bottom:4px;font-size:.95rem;color:#1e1e1e'>{icon} {header}</div>"
            f"<div style='font-size:.92rem;color:#333;line-height:1.5'>{_md_inline_to_html(body)}</div>"
            f"</div>",
            unsafe_allow_html=True,
        )

# ----------------------------------------------------------------------
# DATA MODEL
# ----------------------------------------------------------------------
START_DATE = date(2026, 11, 1)
STATE_FILE = "chefp_state.json"

PHASES = {
    "Machine Learning": [
        ("Python fluency & DS&A refresh", 3),
        ("Math for ML", 3),
        ("Classical ML", 4),
        ("ML from scratch", 3),
        ("Deep learning foundations", 4),
        ("Applied / production-adjacent ML", 3),
    ],
    "MLOps": [
        ("Docker & reproducibility", 3),
        ("Experiment tracking & data versioning", 4),
        ("CI/CD for ML", 3),
        ("Monitoring & drift", 4),
        ("Serving & scaling", 4),
    ],
    "AI Engineer": [
        ("LLM fundamentals", 4),
        ("Prompting, RAG, agents", 5),
        ("LLM apps in production", 4),
        ("Advanced / research-grade ML", 5),
        ("Systems thinking for interviews", 4),
    ],
    "Polish & Interview Prep": [
        ("Portfolio, resume, mock interviews", 5),
    ],
}

STATUS_COLORS = {
    "pending": {"fill": "#fef3b0", "border": "#1e1e1e"},
    "learning": {"fill": "#ede9fe", "border": "#7c3aed"},
    "done": {"fill": "#d7f7e0", "border": "#1e9e5a"},
    "skip": {"fill": "#e9e9ea", "border": "#8a8a8a"},
}
BADGE_COLORS = {
    "repo": "#24292e", "video": "#a855f7", "book": "#059669",
    "course": "#eab308", "note": "#6b7280",
    "doc": "#0284c7", "paper": "#ea580c",
}

# How the resource panel is grouped, so it reads as: watch -> read -> build
RESOURCE_GROUPS = [
    ("▶ Watch & learn", ("video", "course")),
    ("📖 Books & papers", ("book", "paper")),
    ("🛠 Repos, docs & practice", ("repo", "doc", "note")),
]

# Per-topic, week-by-week breakdown: what that specific week focuses on,
# and the concepts/libraries covered that week (mirrors roadmap.sh's
# topic -> sub-topic -> concept structure). List length per topic must
# match that topic's week count in PHASES.
CURRICULUM = {
    "Python fluency & DS&A refresh": [
        ("Python Fundamentals", ["Syntax & Data Types", "Control Flow", "Functions & Modules", "List/Dict Comprehensions"]),
        ("Data Structures & Algorithms", ["Arrays & Strings", "Hash Maps", "Trees & Graphs", "Big-O Complexity"]),
        ("Pythonic Tooling", ["NumPy Basics", "Pandas Basics", "Virtual Envs & pip", "Git & Version Control"]),
    ],
    "Math for ML": [
        ("Linear Algebra", ["Vectors & Matrices", "Matrix Multiplication", "Eigenvalues & Eigenvectors", "SVD"]),
        ("Calculus", ["Derivatives & Gradients", "Chain Rule", "Partial Derivatives", "Gradient Descent Intuition"]),
        ("Probability & Statistics", ["Probability Basics", "Distributions", "Bayes' Theorem", "Hypothesis Testing"]),
    ],
    "Classical ML": [
        ("Regression", ["Linear Regression", "Regularization (L1/L2)", "Polynomial Regression"]),
        ("Classification", ["Logistic Regression", "k-NN", "Decision Trees", "SVMs"]),
        ("Ensemble Methods", ["Random Forests", "Gradient Boosting", "XGBoost / LightGBM"]),
        ("Model Evaluation", ["Cross-Validation", "Precision / Recall / F1", "ROC-AUC", "Bias-Variance Tradeoff"]),
    ],
    "ML from scratch": [
        ("Implementing Regression", ["Linear Regression from Scratch", "Gradient Descent Implementation"]),
        ("Implementing Classifiers", ["k-NN from Scratch", "Decision Tree from Scratch"]),
        ("Implementing Neural Nets", ["Perceptron from Scratch", "Backpropagation by Hand"]),
    ],
    "Deep learning foundations": [
        ("Neural Network Basics", ["Perceptrons", "Activation Functions", "Forward Propagation"]),
        ("Training Neural Nets", ["Backpropagation", "Loss Functions", "Optimizers (SGD, Adam)"]),
        ("Convolutional Networks", ["Convolutions & Pooling", "CNN Architectures", "Image Classification"]),
        ("Sequence Models", ["RNNs & LSTMs", "Sequence-to-Sequence", "Attention Basics"]),
    ],
    "Applied / production-adjacent ML": [
        ("Feature Engineering", ["Feature Scaling", "Encoding Categoricals", "Feature Selection"]),
        ("Model Packaging", ["Saving / Loading Models", "Building an Inference API", "FastAPI Basics"]),
        ("End-to-End Project", ["Data Pipeline", "Train / Serve Split", "Basic Deployment"]),
    ],
    "Docker & reproducibility": [
        ("Docker Fundamentals", ["Images & Containers", "Dockerfile Basics", "Volumes & Networking"]),
        ("Reproducible Environments", ["Requirements Pinning", "Conda vs venv", "Multi-stage Builds"]),
        ("Docker Compose", ["Compose Basics", "Multi-container Apps", "Local Dev Environments"]),
    ],
    "Experiment tracking & data versioning": [
        ("MLflow Basics", ["Tracking Experiments", "Logging Metrics & Params", "Model Registry"]),
        ("Data Versioning", ["DVC Basics", "Versioning Datasets", "Pipeline Reproducibility"]),
        ("Hyperparameter Tracking", ["Grid / Random Search", "Optuna Basics", "Comparing Runs"]),
        ("Reproducible Pipelines", ["Config Management", "Seed Control", "Experiment Reports"]),
    ],
    "CI/CD for ML": [
        ("CI Fundamentals", ["GitHub Actions Basics", "Automated Testing", "Linting & Formatting"]),
        ("CD for ML Models", ["Automated Retraining Triggers", "Model Validation Gates"]),
        ("Testing ML Code", ["Unit Tests for Pipelines", "Data Validation Tests", "Integration Tests"]),
    ],
    "Monitoring & drift": [
        ("Monitoring Basics", ["Logging & Metrics", "Dashboards (Grafana)", "Alerting"]),
        ("Data Drift", ["Covariate Shift", "PSI & KS Tests", "Drift Detection Tools"]),
        ("Model Drift", ["Concept Drift", "Performance Decay Tracking", "Retraining Triggers"]),
        ("Observability", ["Tracing Requests", "Error Budgets", "Incident Response"]),
    ],
    "Serving & scaling": [
        ("Model Serving Basics", ["REST APIs for Models", "Batch vs Real-time Inference"]),
        ("Scalable Serving", ["Load Balancing", "Horizontal Scaling", "Caching"]),
        ("Serving Frameworks", ["TorchServe / TF Serving", "ONNX Runtime", "Triton Inference Server"]),
        ("Cost & Latency Optimization", ["Model Quantization", "Batching Requests", "Autoscaling"]),
    ],
    "LLM fundamentals": [
        ("Transformer Architecture", ["Attention Mechanism", "Self-Attention", "Positional Encoding"]),
        ("Tokenization & Embeddings", ["BPE Tokenization", "Word / Token Embeddings", "Vector Similarity"]),
        ("Pretraining & Fine-tuning", ["Pretraining Objectives", "Fine-tuning Basics", "LoRA / QLoRA"]),
        ("LLM Evaluation", ["Perplexity", "Benchmark Suites", "Human vs Automated Eval"]),
    ],
    "Prompting, RAG, agents": [
        ("Prompt Engineering", ["Zero / Few-shot Prompting", "Chain-of-Thought", "Prompt Templates"]),
        ("Embeddings & Vector Search", ["Embedding Models", "Vector Databases", "Similarity Search"]),
        ("RAG Fundamentals", ["Retrieval Pipelines", "Chunking Strategies", "Reranking"]),
        ("Advanced RAG", ["Hybrid Search", "Query Rewriting", "Multi-hop Retrieval"]),
        ("Agents", ["Tool Use & Function Calling", "ReAct Pattern", "Multi-agent Systems"]),
    ],
    "LLM apps in production": [
        ("Serving LLM Apps", ["FastAPI for LLM Services", "Streaming Responses", "Async Handling"]),
        ("LLM Ops", ["Prompt Versioning", "Cost Tracking", "Latency Optimization"]),
        ("Guardrails & Safety", ["Output Validation", "Content Filtering", "Rate Limiting"]),
        ("Evaluation in Production", ["A/B Testing Prompts", "User Feedback Loops", "Logging & Tracing"]),
    ],
    "Advanced / research-grade ML": [
        ("Graph Neural Networks", ["Message Passing", "GCNs / GATs", "Heterogeneous Graphs"]),
        ("Physics-Informed ML", ["PINNs Basics", "Neural ODEs", "Simulation Surrogates"]),
        ("Generative Models", ["VAEs", "GANs", "Diffusion Models"]),
        ("Federated & Efficient Learning", ["Federated Learning Basics", "Model Distillation", "Quantization"]),
        ("Reading Research Papers", ["Paper Reading Method", "Reproducing Results", "Writing Technical Reports"]),
    ],
    "Systems thinking for interviews": [
        ("ML System Design", ["Design Framework", "Requirements Gathering", "Trade-off Analysis"]),
        ("Case Studies", ["Recommender System Design", "Search Ranking Design", "Fraud Detection Design"]),
        ("Behavioral & Portfolio Prep", ["STAR Method", "Project Storytelling"]),
        ("Mock Interviews", ["System Design Mock", "Coding Mock", "ML Theory Mock"]),
    ],
    "Portfolio, resume, mock interviews": [
        ("Resume & LinkedIn", ["Resume Structure", "Quantifying Impact", "LinkedIn Optimization"]),
        ("Portfolio Site", ["Project Write-ups", "GitHub README Polish", "Personal Site Deploy"]),
        ("Technical Interview Prep", ["Coding Practice", "ML Theory Review"]),
        ("System Design Prep", ["Mock System Design Rounds", "Feedback Iteration"]),
        ("Final Mock Interviews & Outreach", ["Full Mock Loop", "Networking / Outreach", "Application Tracking"]),
    ],
}

# Flatten into a single ordered week list, each tagged with its phase, topic,
# and this specific week's focus + concepts from CURRICULUM.
ALL_WEEKS = []
_wi = 0
for phase, topics in PHASES.items():
    for topic, count in topics:
        week_entries = CURRICULUM[topic]
        assert len(week_entries) == count, f"CURRICULUM mismatch for {topic}"
        for week_label, concepts in week_entries:
            ALL_WEEKS.append({
                "id": _wi, "phase": phase, "topic": topic,
                "week_label": week_label, "concepts": concepts,
            })
            _wi += 1
TOTAL_WEEKS = len(ALL_WEEKS)


def week_dates(i):
    start = START_DATE + timedelta(weeks=i)
    end = start + timedelta(days=6)
    return f"{start.strftime('%b %d')} – {end.strftime('%b %d, %Y')}"


# ----------------------------------------------------------------------
# STATE (persisted to a JSON file next to the app)
# ----------------------------------------------------------------------
def default_week_state():
    return {"status": "pending", "days": [False] * 7, "daily": "", "capstone": "", "last_touched": ""}


def touch_week(wk):
    """Stamp a week as edited today — this is what powers the 'did I make
    progress today' check in the Today banner."""
    wk["last_touched"] = date.today().isoformat()


def _fill_defaults(weeks):
    for w in ALL_WEEKS:
        key = str(w["id"])
        if key not in weeks:
            weeks[key] = default_week_state()
        else:
            weeks[key].setdefault("last_touched", "")
    return weeks


def _read_local(path):
    if os.path.exists(path):
        try:
            with open(path) as f:
                return json.load(f)
        except Exception:
            return None
    return None


def _write_local(path, data):
    try:
        with open(path, "w") as f:
            json.dump(data, f)
    except Exception:
        pass  # a failed local backup must never crash the app


def diagnose_supabase():
    """Plain-English reason the cloud connection is failing + what to do.
    Only runs after a failed load, so it costs nothing normally."""
    from urllib.parse import urlparse
    import socket
    u = urlparse(str(SUPABASE_URL or ""))
    host = u.hostname
    if not u.scheme or not host:
        return ("**What's wrong:** `SUPABASE_URL` isn't a valid web address. It must look like "
                "`https://abcdefghijkl.supabase.co` — copy it from Supabase → Project Settings → API → "
                "**Project URL** (check for a missing `https://`, stray spaces, or extra quotes).")
    project_ref = host.split(".")[0]
    if re.fullmatch(r"x{4,}|your[-_]?project.*|abcdefghijkl", project_ref):
        return (f"**What's wrong:** `SUPABASE_URL` still has the placeholder value (`{host}`). Replace it with your "
                "real **Project URL** from Supabase → Project Settings → API.")
    try:
        socket.getaddrinfo(host, 443)
    except Exception:
        return (f"**What's wrong:** this computer can't find `{host}` on the internet (DNS lookup failed). "
                "Most likely, in this order:\n\n"
                "1. **Typo in the project ID** inside `SUPABASE_URL` — compare it character by character with "
                "Supabase → Project Settings → API → Project URL.\n"
                "2. **The project is paused** (free projects pause after ~1 week idle) — open your Supabase "
                "dashboard and click **Restore project**.\n"
                "3. **Your network/DNS** is blocking it — try another network or turn any VPN off.\n\n"
                f"**30-second test:** paste `{str(SUPABASE_URL).rstrip('/')}/rest/v1/` into your browser. A short JSON "
                "message means the address is fine; \"site can't be reached\" means it's wrong or paused.")
    try:
        r = requests.get(str(SUPABASE_URL).rstrip("/") + "/rest/v1/chefp_roadmap",
                         headers={"apikey": str(SUPABASE_KEY), "Authorization": f"Bearer {SUPABASE_KEY}"},
                         params={"select": "id", "limit": "1"}, timeout=6)
    except Exception as e:
        return f"`{host}` resolves, but the request failed: `{e}`."
    if r.status_code == 200:
        return "The connection works now — press **Retry connection**."
    if r.status_code in (401, 403):
        return ("**What's wrong:** Supabase rejected the key. `SUPABASE_KEY` should be the **service_role** key "
                "(Project Settings → API), pasted without quotes inside the quotes or extra spaces.")
    if r.status_code == 404:
        return ("**What's wrong:** the table doesn't exist yet. Run the SQL from `SUPABASE_SETUP.md` in Supabase's SQL Editor.")
    return f"Supabase answered with HTTP {r.status_code}."


def load_state():
    """Cloud first; if the cloud can't be reached, fall back to the local
    backup (never to a blank state), and remember the cloud is down so we
    don't later overwrite good cloud data with stale/blank data."""
    st.session_state.remote_ok = True
    data = None
    if USE_SUPABASE:
        try:
            res = _supabase.table("chefp_roadmap").select("data").eq("id", _ROW_ID).execute()
            data = res.data[0]["data"] if res.data else {}
            _write_local(STATE_FILE, data)  # keep a fresh local backup
        except Exception as e:
            st.session_state.remote_ok = False
            st.session_state.remote_error = str(e)
    if data is None:
        data = _read_local(STATE_FILE) or {}
    return {"weeks": _fill_defaults(data.get("weeks", {})), "engineering_log": data.get("engineering_log", {})}


def save_state(state):
    _write_local(STATE_FILE, state)  # local backup on EVERY save, no matter what
    if USE_SUPABASE and st.session_state.get("remote_ok", True):
        try:
            _supabase.table("chefp_roadmap").upsert({"id": _ROW_ID, "data": state}).execute()
        except Exception as e:
            st.warning(f"Couldn't sync to Supabase just now ({e}). Your change is safe in the local backup "
                       "and will sync on your next change.")


# ----------------------------------------------------------------------
# ASSIGNMENT SUBMISSIONS STORAGE
# Kept in its OWN row (Supabase) / file (local) so file uploads never make
# the frequent roadmap saves (every checkbox click) heavy. Same table, no
# new setup. Files are stored base64-encoded; 3 MB per file keeps it snappy
# — put anything bigger on GitHub/Drive and submit the link instead.
# ----------------------------------------------------------------------
SUBMISSIONS_FILE = "chefp_submissions.json"
_SUB_ROW_ID = "chefp_submissions"
MAX_FILE_BYTES = 3 * 1024 * 1024
SUBMIT_FILE_TYPES = ["png", "jpg", "jpeg", "gif", "webp", "svg", "pdf", "txt", "md",
                     "py", "ipynb", "csv", "json", "zip", "docx"]


def load_submissions():
    data = None
    if USE_SUPABASE and st.session_state.get("remote_ok", True):
        try:
            res = _supabase.table("chefp_roadmap").select("data").eq("id", _SUB_ROW_ID).execute()
            data = res.data[0]["data"] if res.data else {}
            _write_local(SUBMISSIONS_FILE, data)
        except Exception as e:
            st.session_state.remote_ok = False
            st.session_state.remote_error = str(e)
    if data is None:
        data = _read_local(SUBMISSIONS_FILE) or {}
    return data


def save_submissions(subs):
    _write_local(SUBMISSIONS_FILE, subs)  # local backup on every save
    if USE_SUPABASE and st.session_state.get("remote_ok", True):
        try:
            _supabase.table("chefp_roadmap").upsert({"id": _SUB_ROW_ID, "data": subs}).execute()
        except Exception as e:
            st.warning(f"Couldn't sync submissions to Supabase just now ({e}). Safe in the local backup.")


def build_submission_zip(sat_iso, week_label, week_sub, assign):
    """One compiled package for the week: submission.md + every uploaded file."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        md = [f"# Assignment submission — week of {sat_iso}: {week_label}\n"]
        if assign.get("deliverable"):
            md.append(f"**Deliverable asked for:** {assign['deliverable']}\n")
        if week_sub.get("submitted_at"):
            md.append(f"**Submitted:** {week_sub['submitted_at']}\n")
        for d in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
            e = week_sub.get("days", {}).get(d, {})
            md.append(f"\n## {d}\n")
            md.append(f"**Assignment:** {assign.get('tasks', {}).get(d, '')}\n")
            md.append(f"**Write-up:**\n\n{e.get('text') or '_(blank)_'}\n")
            md.append(f"**Link:** {e.get('link') or '_(none)_'}\n")
            if e.get("files"):
                md.append("**Files:**\n")
                for fobj in e["files"]:
                    safe = re.sub(r"[^A-Za-z0-9._-]", "_", os.path.basename(fobj["name"]))
                    z.writestr(f"files/{d}_{safe}", base64.b64decode(fobj["b64"]))
                    md.append(f"- files/{d}_{safe}\n")
        z.writestr("submission.md", "\n".join(md))
    return buf.getvalue()


if "state" not in st.session_state:
    st.session_state.state = load_state()

state = st.session_state.state

if "subs" not in st.session_state:
    st.session_state.subs = load_submissions()
subs = st.session_state.subs

# ----------------------------------------------------------------------
# GITHUB COMMIT STREAK
# Reads your public push events for free, with no setup. Add GITHUB_TOKEN
# to secrets (a personal access token, "repo" scope) if you want PRIVATE
# repo commits counted too — without it, only public-repo pushes show.
# Change GITHUB_USERNAME below if this isn't your GitHub handle.
# ----------------------------------------------------------------------
GITHUB_USERNAME = "yourfavCHEFP"
GITHUB_TOKEN = _get_secret("GITHUB_TOKEN")


@st.cache_data(ttl=300)
def get_github_push_dates(username, token):
    """Returns the set of ISO dates (UTC) on which at least one push event
    happened, from GitHub's events API (last ~90 days / 300 events)."""
    url = f"https://api.github.com/users/{username}/events" if token \
        else f"https://api.github.com/users/{username}/events/public"
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    dates = set()
    try:
        for page in (1, 2, 3):
            resp = requests.get(url, headers=headers, params={"per_page": 100, "page": page}, timeout=6)
            if resp.status_code != 200:
                break
            events = resp.json()
            if not events:
                break
            for e in events:
                if e.get("type") == "PushEvent":
                    dates.add(e["created_at"][:10])  # "YYYY-MM-DD"
            if len(events) < 100:
                break
    except Exception:
        return None  # signals "couldn't check" vs. genuinely zero
    return dates


def compute_streak(push_dates):
    if not push_dates:
        return 0
    streak = 0
    d = date.today()
    while d.isoformat() in push_dates:
        streak += 1
        d -= timedelta(days=1)
    return streak


# ----------------------------------------------------------------------
# DAILY STUDY PLAN
# Deterministic, rule-based split of a week's concepts + resources across
# 7 days — no AI call, so it's free and instant. Order is preserved
# (watch -> read -> practice) so nothing is assigned half-finished, and
# each resource appears on exactly one day. Saturday is reserved for the
# Engineering Log; Sunday is light review / catch-up.
# ----------------------------------------------------------------------
def build_daily_plan(concepts, resources):
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    plan = {d: {"concept": None, "resources": []} for d in days}
    study_days = days[:5]  # Mon-Fri

    for i, d in enumerate(study_days):
        if concepts:
            plan[d]["concept"] = concepts[i % len(concepts)]

    # watch -> read -> practice, in that order, chunked evenly across
    # Mon-Fri so each resource lands on exactly one day
    ordered = [r for r in resources if r[0] in ("video", "course")] \
        + [r for r in resources if r[0] in ("book", "paper")] \
        + [r for r in resources if r[0] in ("repo", "doc", "note")]
    n = len(ordered)
    if n:
        base, extra = divmod(n, 5)
        idx = 0
        for i, d in enumerate(study_days):
            take = base + (1 if i < extra else 0)
            plan[d]["resources"] = ordered[idx:idx + take]
            idx += take

    plan["Sat"]["note"] = "📓 Engineering Log + 📤 submit this week's assignments — both sections are at the top of the page."
    plan["Sun"]["note"] = "Rest, or catch up on anything left over from the week."
    return plan

# ----------------------------------------------------------------------
# PAGE
# ----------------------------------------------------------------------
st.set_page_config(page_title="CHEF_P Roadmap Tracker", layout="wide")
st.markdown(
    """
    <style>
    /* status pill row: color the ACTIVE (primary) pill per status, keep
       inactive ones as plain neutral outline pills */
    [class*="st-key-status_pending_"] button[data-testid="stBaseButton-primary"] {
        background:#fef3b0 !important; border:2px solid #1e1e1e !important; color:#1e1e1e !important; }
    [class*="st-key-status_learning_"] button[data-testid="stBaseButton-primary"] {
        background:#ede9fe !important; border:2px solid #7c3aed !important; color:#1e1e1e !important; }
    [class*="st-key-status_done_"] button[data-testid="stBaseButton-primary"] {
        background:#d7f7e0 !important; border:2px solid #1e9e5a !important; color:#1e1e1e !important; }
    [class*="st-key-status_skip_"] button[data-testid="stBaseButton-primary"] {
        background:#e9e9ea !important; border:2px solid #8a8a8a !important; color:#1e1e1e !important;
        text-decoration:line-through; }
    [class*="st-key-status_"] button[data-testid="stBaseButton-secondary"] {
        background:#fff !important; border:2px solid #ddd !important; color:#555 !important; }
    [class*="st-key-status_"] button {
        border-radius:20px !important; font-weight:700 !important; width:100% !important; }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    "<h1 style='font-family:Georgia,serif'>CHEF_P — ML/AI Roadmap</h1>"
    "<p style='color:#555'>Machine Learning → MLOps → AI Engineer, "
    "with your own repos/videos/books attached to each topic</p>",
    unsafe_allow_html=True,
)

done_count = sum(1 for w in ALL_WEEKS if state["weeks"][str(w["id"])]["status"] == "done")
st.progress(done_count / TOTAL_WEEKS)
st.caption(f"{done_count}/{TOTAL_WEEKS} weeks marked Done ({round(100*done_count/TOTAL_WEEKS)}%)")
_remote_ok = st.session_state.get("remote_ok", True)
if USE_SUPABASE and _remote_ok:
    st.caption("💾 Saving to Supabase (persists across restarts) + a local backup copy")
elif USE_SUPABASE:
    st.caption("🔴 Supabase unreachable — saving to a local backup file only (cloud data is protected, not overwritten)")
else:
    st.caption("⚠️ Saving to a local file only — will NOT survive a Streamlit Cloud restart. Add SUPABASE_URL/SUPABASE_KEY to secrets.")

if USE_SUPABASE and not _remote_ok:
    with st.container(border=True):
        st.error("☁️ Can't reach Supabase — your progress is NOT syncing to the cloud right now.")
        st.markdown(diagnose_supabase())
        st.caption("Meanwhile, everything you do is saved to a local backup file on this machine, and your existing "
                   "cloud data is protected from being overwritten. Fix the cause above, then retry.")
        if st.button("🔄 Retry connection", key="retry_supabase"):
            for k in ("state", "subs", "remote_ok", "remote_error"):
                st.session_state.pop(k, None)
            st.rerun()
st.markdown(
    "🟡 Pending &nbsp;&nbsp; 🟣 Learning &nbsp;&nbsp; 🟢 Done &nbsp;&nbsp; ⚪ Skip",
    unsafe_allow_html=True,
)

CURRENT_WEEK_ID = max(0, min(TOTAL_WEEKS - 1, (date.today() - START_DATE).days // 7))
TODAY_ISO = date.today().isoformat()

# ---- Today banner: did I touch the roadmap today, and did I commit to
#      GitHub today? Checked live every time the app is opened. ----
progressed_today = any(w["last_touched"] == TODAY_ISO for w in state["weeks"].values())
push_dates = get_github_push_dates(GITHUB_USERNAME, GITHUB_TOKEN)
with st.container(border=True):
    bcols = st.columns(3)
    with bcols[0]:
        st.markdown(f"**📅 Today — {date.today().strftime('%A, %b %d')}**")
    with bcols[1]:
        st.markdown("🟢 Roadmap progress logged" if progressed_today else "⚪ No roadmap activity yet today")
    with bcols[2]:
        if push_dates is None:
            st.markdown(f"❓ Couldn't reach GitHub for `{GITHUB_USERNAME}`")
        elif TODAY_ISO in push_dates:
            st.markdown(f"🟢 Committed today · streak: {compute_streak(push_dates)} day(s)")
        else:
            st.markdown("🔴 No commits yet today")
    if push_dates is None:
        st.caption("GitHub check failed — rate-limited, username wrong, or offline. "
                   "Add `GITHUB_TOKEN` to secrets for private-repo commits to count too.")

# ---- Engineering Log: a private weekly write-up (what broke, how you
#      fixed it, what you built), stored alongside your roadmap data and
#      downloadable as one Markdown file any time. ----
_d = date.today()
current_saturday = _d - timedelta(days=(_d.weekday() - 5) % 7)  # most recent Saturday (today, if today is one)
sat_iso = current_saturday.isoformat()
log = state.setdefault("engineering_log", {})

with st.expander(f"📓 Engineering Log — week of {current_saturday.strftime('%b %d, %Y')}", expanded=False):
    entry = log.get(sat_iso, {"went_wrong": "", "how_fixed": "", "what_built": ""})
    went_wrong = st.text_area("What went wrong this week? (errors, bugs, mathematical confusion)",
                               value=entry["went_wrong"], key=f"log_wrong_{sat_iso}")
    how_fixed = st.text_area("How did you fix or unblock it?",
                              value=entry["how_fixed"], key=f"log_fixed_{sat_iso}")
    what_built = st.text_area("What did you successfully build?",
                               value=entry["what_built"], key=f"log_built_{sat_iso}")
    if st.button("Save this week's log entry", key="save_log"):
        log[sat_iso] = {"went_wrong": went_wrong, "how_fixed": how_fixed, "what_built": what_built}
        save_state(state)
        st.success("Saved.")

    past = sorted((k for k in log if k != sat_iso), reverse=True)
    if past:
        st.markdown("---")
        st.caption("Past entries")
        for k in past:
            e = log[k]
            with st.expander(k, expanded=False):
                st.markdown(f"**What went wrong:** {e['went_wrong'] or '_(blank)_'}")
                st.markdown(f"**How you fixed it:** {e['how_fixed'] or '_(blank)_'}")
                st.markdown(f"**What you built:** {e['what_built'] or '_(blank)_'}")

    if log:
        md_lines = ["# CHEF_P — Engineering Log\n"]
        for k in sorted(log, reverse=True):
            e = log[k]
            md_lines.append(f"## Week of {k}\n")
            md_lines.append(f"**What went wrong:** {e['went_wrong'] or '_(blank)_'}\n")
            md_lines.append(f"**How you fixed it:** {e['how_fixed'] or '_(blank)_'}\n")
            md_lines.append(f"**What you built:** {e['what_built'] or '_(blank)_'}\n")
        st.download_button("⬇ Download full log as Markdown", "\n".join(md_lines),
                            file_name="chefp_engineering_log.md", mime="text/markdown")

# ---- Weekly Assignment Submission (Saturday): the 5 daily assignments for
#      this calendar week, compiled in one place. Text + link + files/diagrams
#      per day, each saved the moment you enter it. ----
sub_wid = max(0, min(TOTAL_WEEKS - 1, (current_saturday - START_DATE).days // 7))
sub_week = ALL_WEEKS[sub_wid]
sub_assign = ASSIGNMENTS.get(sub_week["week_label"], {})
week_sub = subs.setdefault(sat_iso, {"days": {}, "submitted_at": ""})
week_sub.setdefault("days", {})
upload_counters = st.session_state.setdefault("upload_counters", {})

with st.expander(f"📤 Weekly Assignment Submission — Week {sub_wid + 1}: {sub_week['week_label']}", expanded=False):
    if week_sub.get("submitted_at"):
        st.success(f"✅ Submitted on {week_sub['submitted_at']} — you can still edit and re-submit.")
    st.caption("Everything below saves automatically the moment you type, paste a link, or upload. "
               "Diagrams: upload an image/PDF, or paste a link (Excalidraw, draw.io, Figma…). "
               "Files over 3 MB: put them on GitHub/Drive and paste the link instead.")
    if sub_assign.get("deliverable"):
        st.info(f"**This week's deliverable:** {sub_assign['deliverable']}")

    any_change = False
    for d in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
        entry = week_sub["days"].setdefault(d, {"text": "", "link": "", "files": []})
        entry.setdefault("files", [])
        st.markdown(f"#### {d}")
        st.markdown(f"📝 {sub_assign.get('tasks', {}).get(d, 'No assignment written for this day.')}")

        text = st.text_area("Write-up / notes / answers", value=entry["text"],
                            key=f"sub_text_{sat_iso}_{d}", height=100)
        link = st.text_input("Link (repo, notebook, deployed app, diagram…)", value=entry["link"],
                             key=f"sub_link_{sat_iso}_{d}")
        if text != entry["text"] or link != entry["link"]:
            entry["text"], entry["link"] = text, link
            any_change = True

        counter = upload_counters.get(f"{sat_iso}_{d}", 0)
        uploaded = st.file_uploader("Upload files or diagrams", accept_multiple_files=True,
                                    type=SUBMIT_FILE_TYPES, key=f"sub_up_{sat_iso}_{d}_{counter}")
        if uploaded:
            for f in uploaded:
                data = f.getvalue()
                if len(data) > MAX_FILE_BYTES:
                    st.error(f"{f.name} is {len(data) / 1e6:.1f} MB — over the 3 MB limit. Submit it as a link instead.")
                    continue
                if any(x["name"] == f.name and x["size"] == len(data) for x in entry["files"]):
                    continue
                entry["files"].append({"name": f.name, "size": len(data),
                                       "b64": base64.b64encode(data).decode()})
                any_change = True
            upload_counters[f"{sat_iso}_{d}"] = counter + 1  # resets the uploader after saving
            touch_week(state["weeks"][str(sub_wid)])
            save_state(state)
            save_submissions(subs)
            st.rerun()

        for fi, fobj in enumerate(list(entry["files"])):
            fc1, fc2, fc3 = st.columns([4, 1, 1])
            fc1.markdown(f"📎 `{fobj['name']}` · {fobj['size'] / 1024:.0f} KB")
            fc2.download_button("⬇", base64.b64decode(fobj["b64"]), file_name=fobj["name"],
                                key=f"dl_{sat_iso}_{d}_{fi}")
            if fc3.button("✕", key=f"rm_{sat_iso}_{d}_{fi}"):
                entry["files"].pop(fi)
                save_submissions(subs)
                st.rerun()
        st.divider()

    if any_change:
        touch_week(state["weeks"][str(sub_wid)])
        save_state(state)
        save_submissions(subs)

    sc1, sc2 = st.columns(2)
    if sc1.button("✅ Submit this week's assignments", key=f"submit_{sat_iso}", type="primary"):
        week_sub["submitted_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        save_submissions(subs)
        st.rerun()
    sc2.download_button("⬇ Download compiled week (.zip)",
                        build_submission_zip(sat_iso, sub_week["week_label"], week_sub, sub_assign),
                        file_name=f"chefp_week_{sat_iso}_submission.zip", mime="application/zip")

    total_bytes = sum(f["size"] for w in subs.values() for dd in w.get("days", {}).values()
                      for f in dd.get("files", []))
    st.caption(f"Stored so far: {total_bytes / 1e6:.1f} MB of uploaded files across all weeks.")
    if total_bytes > 15e6:
        st.warning("You're past 15 MB of stored files — prefer links for large items to keep the app fast.")
    past_subs = sorted((k for k in subs if k != sat_iso), reverse=True)
    if past_subs:
        st.markdown("**Past weeks:** " + " · ".join(
            f"{'✅' if subs[k].get('submitted_at') else '⏳'} {k}" for k in past_subs))

# ---- single source of truth for "what's open right now" is the URL's
#      ?week= param, not st.tabs (tabs reset on a real page navigation,
#      which is what clicking a diagram node causes) ----
week_qp = st.query_params.get("week")
try:
    open_wid = int(week_qp) - 1
    if not (0 <= open_wid < TOTAL_WEEKS):
        open_wid = CURRENT_WEEK_ID
except (TypeError, ValueError):
    open_wid = CURRENT_WEEK_ID
open_concept = st.query_params.get("concept")  # None unless a leaf node was clicked

phase_name = next(w["phase"] for w in ALL_WEEKS if w["id"] == open_wid)
topics = PHASES[phase_name]
phase_week_ids = [w["id"] for w in ALL_WEEKS if w["phase"] == phase_name]

# ---- phase switcher: real links (so it works from inside the SVG's
#      navigation model too), first week of each phase ----
phase_links = []
for pname, ptopics in PHASES.items():
    first_wid = next(w["id"] for w in ALL_WEEKS if w["phase"] == pname)
    active = pname == phase_name
    style = ("color:inherit;font-weight:700;border-bottom:2px solid #e74c3c;" if active
             else "color:#888;font-weight:600;")
    phase_links.append(
        f"<a href='?week={first_wid+1}' target='_top' "
        f"style='{style}text-decoration:none;padding:6px 14px;display:inline-block'>{pname}</a>"
    )
st.markdown(
    f"<div style='border-bottom:1px solid #eee;margin-bottom:14px'>{''.join(phase_links)}</div>",
    unsafe_allow_html=True,
)

# ---- week picker (kept for accessibility / not everyone wants to click
#      a diagram) — stays in sync with the URL either direction ----
options = {
    f"Week {wid + 1} · {week_dates(wid)} — "
    f"{ALL_WEEKS[wid]['week_label']}": wid
    for wid in phase_week_ids
}
option_labels = list(options.keys())
default_index = phase_week_ids.index(open_wid)
choice = st.selectbox("Open a week to edit", option_labels, index=default_index, key=f"sel_{phase_name}")
wid = options[choice]
if wid != open_wid:
    st.query_params["week"] = str(wid + 1)
    if "concept" in st.query_params:
        del st.query_params["concept"]
    st.rerun()

wk = state["weeks"][str(wid)]
week_meta = ALL_WEEKS[wid]
topic_label = week_meta["topic"]
week_focus = week_meta["week_label"]
week_concepts = week_meta["concepts"]

# topic index within phase (for the "part of" line) and week's
# position within its own topic block
topic_total = next(c for t, c in topics if t == topic_label)
weeks_of_topic = [w["id"] for w in ALL_WEEKS if w["phase"] == phase_name and w["topic"] == topic_label]
week_in_topic = weeks_of_topic.index(wid) + 1

week_resources = WEEK_RESOURCES.get(week_focus, [])
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown(
        f"<div style='background:#1e1e1e;color:#fff;padding:9px 16px;border-radius:10px;"
        f"display:flex;justify-content:space-between;align-items:center;font-size:.82rem;margin-bottom:10px'>"
        f"<span>📅 Week {wid + 1} · {week_dates(wid)}</span>"
        f"<span style='opacity:.75'>{phase_name}</span></div>",
        unsafe_allow_html=True,
    )
    st.caption(f"{topic_label} — part {week_in_topic} of {topic_total}")
    st.markdown(f"## {week_focus}")
    st.markdown(" &nbsp;·&nbsp; ".join(f"`{c}`" for c in week_concepts))

    # ---- Daily study plan: this week's concepts + resources, pre-split
    #      across the 7 days so there's no daily "what do I study?" delay.
    #      Nothing is fragmented — each resource lands on exactly one day. ----
    with st.expander("📅 This week's daily study plan", expanded=(wid == CURRENT_WEEK_ID)):
        daily_plan = build_daily_plan(week_concepts, week_resources)
        today_label = date.today().strftime("%a") if wid == CURRENT_WEEK_ID else None
        for d, slot in daily_plan.items():
            is_today = d == today_label
            head = f"**{'👉 ' if is_today else ''}{d}"
            head += f" — {slot['concept']}**" if slot["concept"] else "**"
            st.markdown(head)
            for rtype, label, url in slot["resources"]:
                color = BADGE_COLORS.get(rtype, "#6b7280")
                badge = (f"<span style='background:{color};color:#fff;font-size:.6rem;"
                         f"font-weight:700;padding:1px 5px;border-radius:4px;margin-right:5px'>{rtype}</span>")
                if url:
                    st.markdown(f"&nbsp;&nbsp;{badge}<a href='{url}' target='_blank'>{label}</a>", unsafe_allow_html=True)
                else:
                    st.markdown(f"&nbsp;&nbsp;{badge}{label}", unsafe_allow_html=True)
            day_task = ASSIGNMENTS.get(week_focus, {}).get("tasks", {}).get(d)
            if day_task:
                st.markdown(f"&nbsp;&nbsp;📝 **Assignment:** {day_task}")
            if slot.get("note"):
                st.caption(slot["note"])
            if not slot["resources"] and not slot.get("note") and not day_task:
                st.caption("Review / catch-up.")
        deliverable = ASSIGNMENTS.get(week_focus, {}).get("deliverable")
        if deliverable:
            st.info(f"**Saturday deliverable:** {deliverable}")

    # ---- Learn with AI: free, hand-written lesson content — no API, no
    #      key, no cost. Written at the week-topic level; clicking a
    #      specific concept still shows that week's lesson (it covers
    #      that concept), with a note saying so. ----
    clicked_concept = open_concept if (open_concept and open_concept in week_concepts) else None
    display_label = clicked_concept or week_focus

    st.markdown("**🤖 Learn with AI**" + (f" — _{display_label}_" if clicked_concept else ""))
    if clicked_concept:
        st.caption(f"Shown as part of the '{week_focus}' lesson, which covers this concept.")
    ai_key_base = f"{wid}_{display_label}"
    ai_cols = st.columns(3)
    for mode, acol in zip(["explain", "teach", "quiz"], ai_cols):
        with acol:
            if st.button(AI_LABELS[mode], key=f"ai_{mode}_{ai_key_base}", width="stretch"):
                st.session_state.setdefault("ai_shown", {})[ai_key_base] = mode
    shown_mode = st.session_state.get("ai_shown", {}).get(ai_key_base)
    if shown_mode == "teach":
        render_teach_lesson(week_focus, get_static_content("teach", week_focus))
    elif shown_mode:
        content = get_static_content(shown_mode, week_focus)
        with st.container(border=True):
            st.markdown(content)

    status_cols = st.columns(4, gap="small")
    statuses = ["pending", "learning", "done", "skip"]
    for s, scol in zip(statuses, status_cols):
        with scol:
            if st.button(s.capitalize(), key=f"status_{s}_{wid}",
                         type="primary" if wk["status"] == s else "secondary",
                         width="stretch"):
                wk["status"] = s
                touch_week(wk)
                save_state(state)
                st.rerun()

    daily = st.text_input("Daily project this week", value=wk["daily"], key=f"daily_{wid}")
    capstone = st.text_input("Capstone project this week", value=wk["capstone"], key=f"cap_{wid}")
    if daily != wk["daily"] or capstone != wk["capstone"]:
        wk["daily"] = daily
        wk["capstone"] = capstone
        touch_week(wk)
        save_state(state)

    st.write("**This week's days**")
    day_cols = st.columns(7)
    days_labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    changed = False
    for i, dcol in enumerate(day_cols):
        with dcol:
            checked = st.checkbox(days_labels[i], value=wk["days"][i], key=f"day_{wid}_{i}")
            if checked != wk["days"][i]:
                wk["days"][i] = checked
                changed = True
    if changed:
        touch_week(wk)
        save_state(state)

with col2:
    st.write("**Attached resources**")
    if not week_resources:
        st.caption("No resources attached to this week yet.")
    for group_title, group_types in RESOURCE_GROUPS:
        items = [r for r in week_resources if r[0] in group_types]
        if not items:
            continue
        st.markdown(f"<div style='font-size:.78rem;font-weight:700;margin:12px 0 2px;opacity:.75'>{group_title}</div>",
                    unsafe_allow_html=True)
        for rtype, label, url in items:
            color = BADGE_COLORS.get(rtype, "#6b7280")
            badge = (f"<span style='background:{color};color:#fff;font-size:.62rem;"
                     f"font-weight:700;padding:2px 6px;border-radius:5px;margin-right:6px'>"
                     f"{rtype}</span>")
            if url:
                st.markdown(f"{badge}<a href='{url}' target='_blank'>{label}</a>", unsafe_allow_html=True)
            else:
                st.markdown(f"{badge}{label}", unsafe_allow_html=True)

# ---- visual map: topic trunk -> that week's specific focus -> the
#      concepts covered that week (mirrors roadmap.sh's 3-level layout).
#      Every week-focus box is a real link — click it to open that week. ----
st.markdown("#### Visual map — click any week to open it")
LEAF_H, GAP, BRANCH_X, LEAF_X = 0.42, 0.4, 3.6, 8.2
g = graphviz.Digraph(engine="neato")
g.attr(bgcolor="white")
g.attr("node", fontname="Helvetica", fontsize="11", shape="box", style="filled,rounded")
g.attr("edge", color="#3b82f6")

y_cursor = 0.0
prev_trunk = None
wi_ptr = 0
for topic, count in topics:
    week_entries = CURRICULUM[topic]
    week_block_heights = [max(len(concepts), 1) * LEAF_H for _, concepts in week_entries]
    topic_block_h = sum(week_block_heights)
    topic_y = y_cursor - topic_block_h / 2
    tid = f"t_{topic}"
    g.node(tid, topic, pos=f"0,{topic_y}!",
           fillcolor="#fef3b0", color="#1e1e1e", penwidth="2")
    if prev_trunk:
        g.edge(prev_trunk, tid, penwidth="2", arrowhead="none")
    prev_trunk = tid

    week_cursor = y_cursor
    for (week_label, concepts), block_h in zip(week_entries, week_block_heights):
        this_wid = phase_week_ids[wi_ptr]
        wi_ptr += 1
        this_wk = state["weeks"][str(this_wid)]
        colors = STATUS_COLORS[this_wk["status"]]
        is_open = this_wid == wid
        week_y = week_cursor - block_h / 2
        node_label = f"Week {this_wid + 1}\n{week_label}" \
            + (" 📍" if this_wid == CURRENT_WEEK_ID else "") + (" ✏️" if is_open else "")
        wnode = f"w{this_wid}"
        g.node(wnode, node_label, pos=f"{BRANCH_X},{week_y}!",
               fillcolor=colors["fill"],
               color="#1e40af" if is_open else colors["border"],
               penwidth="4" if is_open else "2",
               URL=f"?week={this_wid + 1}", target="_blank")
        g.edge(tid, wnode, style="dotted", arrowhead="none")

        leaf_cursor = week_cursor
        for concept in concepts:
            ly = leaf_cursor - LEAF_H / 2
            lnode = f"l{this_wid}_{concept}"
            is_open_concept = is_open and open_concept == concept
            leaf_url = f"?week={this_wid + 1}&concept={urllib.parse.quote(concept)}"
            g.node(lnode, concept, pos=f"{LEAF_X},{ly}!",
                   fillcolor="#ffe9a8" if is_open_concept else "#fdf0d5",
                   color="#1e40af" if is_open_concept else "#a67c00",
                   penwidth="3" if is_open_concept else "1",
                   fontsize="9", width="0", height="0",
                   URL=leaf_url, target="_blank")
            g.edge(wnode, lnode, style="dotted", color="#a67c00", arrowhead="none")
            leaf_cursor -= LEAF_H

        week_cursor -= block_h
    y_cursor -= topic_block_h + GAP

svg = g.pipe(format="svg").decode("utf-8")
st.iframe(svg, height="content", width="stretch")
