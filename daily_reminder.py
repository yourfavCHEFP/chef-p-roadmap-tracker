"""
Runs on a schedule via GitHub Actions (see .github/workflows/daily-reminder.yml).
Checks whether you touched the roadmap today and whether you committed to
GitHub today, then sends a free push notification via ntfy.sh — this is
what actually reaches you even if you never open the Streamlit app that day.

Needed as GitHub Actions repo secrets (Settings -> Secrets and variables ->
Actions -> New repository secret):
  SUPABASE_URL     - same value as in your Streamlit app's secrets
  SUPABASE_KEY     - same value as in your Streamlit app's secrets
  NTFY_TOPIC       - a topic name you invent, e.g. "chefp-roadmap-x7q2"
                     (pick something unguessable, since anyone who knows a
                     public ntfy.sh topic name can read its messages)
  GITHUB_TOKEN_PAT - optional, a personal access token (repo scope) if you
                     want private-repo commits to count; falls back to
                     public-only if not set
"""
import os
import sys
from datetime import date, timedelta

import requests

GITHUB_USERNAME = "yourfavCHEFP"
TOTAL_WEEKS = 65
START_DATE = date(2026, 10, 1)


def get_state():
    url = os.environ["SUPABASE_URL"].rstrip("/") + "/rest/v1/chefp_roadmap"
    key = os.environ["SUPABASE_KEY"]
    headers = {"apikey": key, "Authorization": f"Bearer {key}"}
    resp = requests.get(url, headers=headers, params={"id": "eq.chefp", "select": "data"}, timeout=10)
    resp.raise_for_status()
    rows = resp.json()
    return rows[0]["data"] if rows else {}


def progressed_today(state, today_iso):
    weeks = state.get("weeks", {})
    return any(w.get("last_touched") == today_iso for w in weeks.values())


def logged_this_saturday(state, saturday_iso):
    return saturday_iso in state.get("engineering_log", {})


def get_github_push_dates(username, token):
    url = f"https://api.github.com/users/{username}/events" if token \
        else f"https://api.github.com/users/{username}/events/public"
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    dates = set()
    for page in (1, 2, 3):
        resp = requests.get(url, headers=headers, params={"per_page": 100, "page": page}, timeout=10)
        if resp.status_code != 200:
            break
        events = resp.json()
        if not events:
            break
        for e in events:
            if e.get("type") == "PushEvent":
                dates.add(e["created_at"][:10])
        if len(events) < 100:
            break
    return dates


def current_week_label():
    wid = max(0, min(TOTAL_WEEKS - 1, (date.today() - START_DATE).days // 7))
    return wid + 1


def send_ntfy(topic, title, message, priority="default"):
    requests.post(
        f"https://ntfy.sh/{topic}",
        data=message.encode("utf-8"),
        headers={"Title": title, "Priority": priority, "Tags": "robot"},
        timeout=10,
    )


def main():
    today = date.today()
    today_iso = today.isoformat()
    saturday_iso = (today - timedelta(days=(today.weekday() - 5) % 7)).isoformat()

    try:
        state = get_state()
    except Exception as e:
        print(f"Could not read Supabase state: {e}", file=sys.stderr)
        state = {}

    token = os.environ.get("GITHUB_TOKEN_PAT")
    try:
        push_dates = get_github_push_dates(GITHUB_USERNAME, token)
    except Exception as e:
        print(f"Could not reach GitHub: {e}", file=sys.stderr)
        push_dates = set()

    did_progress = progressed_today(state, today_iso)
    did_commit = today_iso in push_dates
    did_log = logged_this_saturday(state, saturday_iso) if today.weekday() == 5 else True

    lines = [
        f"Week {current_week_label()} of {TOTAL_WEEKS}",
        ("✅" if did_progress else "❌") + " Roadmap progress today",
        ("✅" if did_commit else "❌") + " GitHub commit today",
    ]
    if today.weekday() == 5:
        lines.append(("✅" if did_log else "❌") + " Engineering Log this week")

    all_good = did_progress and did_commit and did_log
    title = "✅ CHEF_P Roadmap — on track" if all_good else "⏰ CHEF_P Roadmap — action needed"
    message = "\n".join(lines)

    topic = os.environ.get("NTFY_TOPIC")
    if not topic:
        print("NTFY_TOPIC not set — printing instead of sending:\n" + title + "\n" + message)
        return
    send_ntfy(topic, title, message, priority="default" if all_good else "high")
    print("Sent:", title, "|", message.replace("\n", " / "))


if __name__ == "__main__":
    main()
