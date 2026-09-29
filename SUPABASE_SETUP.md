# Supabase setup (one-time, ~5 minutes)

1. Go to https://supabase.com → sign up (free tier is enough) → "New project."
2. Once it's created, open **SQL Editor** (left sidebar) → New query → paste and run:

```sql
create table if not exists chefp_roadmap (
  id text primary key,
  data jsonb not null,
  updated_at timestamptz default now()
);
```

3. Go to **Project Settings → API**. Copy two values:
   - **Project URL** (looks like `https://xxxxxxxx.supabase.co`)
   - **service_role key** (NOT the "anon" key — service_role has full read/write and is only ever used server-side, which is exactly what this app does)

4. In your Streamlit Cloud app: **App settings → Secrets**, paste:

```toml
SUPABASE_URL = "https://xxxxxxxx.supabase.co"
SUPABASE_KEY = "paste-your-service_role-key-here"
```

5. Save. Streamlit Cloud restarts the app automatically with the secrets available — you'll see the caption at the top switch from
   "⚠️ Saving to a local file only" to "💾 Saving to Supabase."

That's it — every status change, checkbox, and text field now writes to that one Supabase row and survives restarts, redeploys, and the app sleeping from inactivity.

**Testing locally before you deploy:** create a file `.streamlit/secrets.toml` in the same folder as `app.py` with the same two lines as above, and add `.streamlit/secrets.toml` to your `.gitignore` so the key never gets committed to GitHub. Without that file present, the app automatically falls back to a local JSON file — so it still works, it just won't be durable until the secrets are set.
