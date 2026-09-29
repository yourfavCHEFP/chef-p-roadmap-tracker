# CHEF_P Roadmap Tracker

An interactive Streamlit app for tracking a 65-week learning plan from machine learning foundations through MLOps, AI engineering, and interview preparation.

## Features

- Browse the roadmap by phase, week, topic, and concept.
- Track weekly progress, daily check-ins, and project notes.
- Explore attached learning resources and built-in written lessons.
- Save progress to Supabase, or use a local JSON file for local development.

## Run Locally

Use Python 3.10 or newer. Install the Python dependencies and Graphviz:

```bash
python -m pip install -r requirements.txt
```

The visual roadmap uses the Graphviz system executable. Install it if it is not already available (for example, `brew install graphviz` on macOS). Then start the app:

```bash
streamlit run app.py
```

Without Supabase secrets, progress is saved in `chefp_state.json` beside the app. That local file is excluded from Git.

## Deploy to Streamlit Community Cloud

1. Push this project to a GitHub repository.
2. In Streamlit Community Cloud, create an app from that repository and select `app.py` as the app file.
3. Add the Supabase secrets described in [SUPABASE_SETUP.md](SUPABASE_SETUP.md) under the app's **Settings > Secrets**.

`requirements.txt` installs the Python dependencies. Streamlit Cloud installs the system Graphviz package using `packages.txt`.

The local JSON fallback is not durable on Streamlit Cloud. Configure Supabase if progress must persist across app restarts and redeployments. Supabase credentials must remain in Streamlit secrets and must never be committed to GitHub. The configured Supabase key is used server-side by the app and has elevated permissions; treat it as a secret.

## Shared Progress

The app currently stores progress in one shared Supabase row and does not have user accounts. Anyone using the deployed app will see and edit the same roadmap progress. Do not use it for private or per-user data without adding authentication and user-scoped storage.
