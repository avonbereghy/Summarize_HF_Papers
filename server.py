#!/usr/bin/env python3
"""
Simple local API to trigger "summarize today" from the UI.

Endpoints:
  - GET  /api/health               -> { ok: true }
  - POST /api/summarize_today      -> runs scrape_hf_papers.py --today and update_data_json.py

Run locally:
  pip install -r requirements.txt
  python server.py

Then open the site via a local web server (for example):
  python -m http.server 8000
and browse http://localhost:8000

Note: requires environment variables for the model provider, e.g.
  TOGETHER_API_KEY or GEMINI_API_KEY / GOOGLE_API_KEY
"""

import json
import subprocess
import sys
from pathlib import Path
from flask import Flask, jsonify
from flask_cors import CORS

ROOT = Path(__file__).resolve().parent

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.get("/api/health")
def health():
    return jsonify({"ok": True})


def run(cmd, cwd: Path):
    proc = subprocess.run(
        cmd,
        cwd=str(cwd),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )
    return proc.returncode, proc.stdout


@app.post("/api/summarize_today")
def summarize_today():
    # 1) Scrape + summarize for today
    code, out1 = run([sys.executable, "scrape_hf_papers.py", "--today"], ROOT)
    if code != 0:
        return (
            jsonify({"ok": False, "step": "scrape", "log": out1}),
            500,
        )

    # 2) Update data.json
    code, out2 = run([sys.executable, "update_data_json.py"], ROOT)
    if code != 0:
        return (
            jsonify({"ok": False, "step": "update_data", "log": out2}),
            500,
        )

    return jsonify({"ok": True, "log": (out1 + "\n" + out2)[-2000:]})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)

