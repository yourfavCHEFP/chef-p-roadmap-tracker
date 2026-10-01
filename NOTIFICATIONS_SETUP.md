# Daily reminder — one-time setup (~10 minutes)

The in-app "Today" banner only works when you open the app. This is the part
that reaches you even if you forget to open it — a real push notification,
sent automatically every day, for $0.

## 1. Install ntfy (2 min)
- Phone: install the **ntfy** app (iOS App Store / Google Play).
- Open it, tap "+", and subscribe to a topic name **you invent** — something
  unguessable, e.g. `chefp-roadmap-x7q2`. Anyone who knows your topic name
  can read your notifications, so don't use something obvious.
- No account, no sign-up, no cost.

## 2. Add repo secrets (5 min)
In your roadmap's GitHub repo: **Settings → Secrets and variables → Actions
→ New repository secret**. Add these four:

| Secret name | Value |
|---|---|
| `SUPABASE_URL` | same value you already put in Streamlit's secrets |
| `SUPABASE_KEY` | same value you already put in Streamlit's secrets |
| `NTFY_TOPIC` | the topic name you invented in step 1 |
| `GITHUB_TOKEN_PAT` | optional — only needed if you want *private* repo commits to count (see below) |

## 3. Push the workflow files
`daily_reminder.py` and `.github/workflows/daily-reminder.yml` (already in
this download) need to be committed to your repo, in that same folder
structure. Once pushed, GitHub runs it automatically every day at 19:00 UTC
(8 PM Nigeria time) — edit the `cron` line in the workflow file if you want
a different hour.

## 4. Test it right now
Go to your repo's **Actions** tab → "CHEF_P Daily Roadmap Reminder" →
**Run workflow**. Within a minute you should get a push notification on
your phone. If you don't, check the workflow's log output for the error.

## About the optional `GITHUB_TOKEN_PAT`
Without it, only commits to **public** repos count toward your streak
(both in-app and in the daily push). If some of your project repos are
private, create a token at **github.com/settings/tokens** → "Generate new
token (classic)" → scope: `repo` → paste it in as `GITHUB_TOKEN_PAT`. Treat
it like a password — never commit it directly into code.

## Honest limitation
GitHub Actions' free scheduled runs can occasionally fire a few minutes
late (never early) — fine for a daily reminder, just don't expect
to-the-second precision.
