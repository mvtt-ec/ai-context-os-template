# AI Context OS Template

Open-source starter for maintaining **one portable source of truth** across ChatGPT, Claude, Gemini, Codex, local AI tools, and workspace apps.

All included data is fictional/sample data.

## Core principle
**One canonical source of truth → controlled target-specific context packets.**

Canonical records live under `context/`; generated packets live under `generated/` and are derivative.

## Quick start
```bash
python3 scripts/validate_repo.py
python3 scripts/build_context.py --target codex
```

## Safe deployment
Use this public repo as a template. Create a **fresh private repo** for real context. Never populate a private repo and later make it public.

## Sensitivity
- `internal`: may export to approved targets
- `confidential`: explicit policy required
- `restricted`: never auto-export

Never store passwords, API keys, refresh tokens, private keys, recovery codes, cookies, or bank credentials in Git.

## License
Apache-2.0.
