"""
CHEF_P Roadmap Tracker — Streamlit app
Machine Learning -> MLOps -> AI Engineer -> Polish & Interview Prep
65 weeks starting Oct 1, 2026.
"""
import json
import os
import re
import urllib.parse
from datetime import date, timedelta

import streamlit as st
import graphviz

from roadmap_content import STATIC_CONTENT, TOPIC_ILLUSTRATIONS
from resources_data import WEEK_RESOURCES

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
START_DATE = date(2026, 10, 1)
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
    return {"status": "pending", "days": [False] * 7, "daily": "", "capstone": ""}


def _fill_defaults(weeks):
    for w in ALL_WEEKS:
        key = str(w["id"])
        if key not in weeks:
            weeks[key] = default_week_state()
    return weeks


def load_state():
    if USE_SUPABASE:
        weeks = {}
        try:
            res = _supabase.table("chefp_roadmap").select("data").eq("id", _ROW_ID).execute()
            if res.data:
                weeks = res.data[0]["data"].get("weeks", {})
        except Exception as e:
            st.warning(f"Could not load saved state from Supabase ({e}). Starting fresh this session.")
        return {"weeks": _fill_defaults(weeks)}
    # local JSON fallback
    data = {}
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE) as f:
                data = json.load(f)
        except Exception:
            data = {}
    return {"weeks": _fill_defaults(data.get("weeks", {}))}


def save_state(state):
    if USE_SUPABASE:
        try:
            _supabase.table("chefp_roadmap").upsert({"id": _ROW_ID, "data": state}).execute()
        except Exception as e:
            st.warning(f"Could not save to Supabase ({e}). Your last change may not have persisted.")
        return
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)


if "state" not in st.session_state:
    st.session_state.state = load_state()

state = st.session_state.state

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
st.caption("💾 Saving to Supabase (persists across restarts)" if USE_SUPABASE
           else "⚠️ Saving to a local file only — will NOT survive a Streamlit Cloud restart. Add SUPABASE_URL/SUPABASE_KEY to secrets.")
st.markdown(
    "🟡 Pending &nbsp;&nbsp; 🟣 Learning &nbsp;&nbsp; 🟢 Done &nbsp;&nbsp; ⚪ Skip",
    unsafe_allow_html=True,
)

CURRENT_WEEK_ID = max(0, min(TOTAL_WEEKS - 1, (date.today() - START_DATE).days // 7))

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
                save_state(state)
                st.rerun()

    daily = st.text_input("Daily project this week", value=wk["daily"], key=f"daily_{wid}")
    capstone = st.text_input("Capstone project this week", value=wk["capstone"], key=f"cap_{wid}")
    if daily != wk["daily"] or capstone != wk["capstone"]:
        wk["daily"] = daily
        wk["capstone"] = capstone
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
        save_state(state)

with col2:
    st.write("**Attached resources**")
    week_resources = WEEK_RESOURCES.get(week_focus, [])
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
