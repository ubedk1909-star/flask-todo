# Flask ToDo App

A beginner-friendly Flask app to test basic Git branching and merging.

## Endpoints
- `/` — Health check
- `/api` — Returns content from `data/api.json`
- `/submittodoitem` — Accepts POST JSON with `itemName` and `itemDescription`

## Run Locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

