# HuggingFace Papers Daily

An interactive web application that provides daily summaries of the latest AI research papers from HuggingFace. Features a calendar interface where users can click on highlighted dates to explore paper summaries and detailed analyses.

The system automatically fetches papers, generates comprehensive summaries using AI, and presents them in an elegant, user-friendly interface with responsive design and smooth animations.

**[View Live Site →](https://avonbereghy.github.io/Summarize_HF_Papers/)**

## Local "Summarize Today" Button

The UI now shows a "Summarize Today" button when there are no papers for today. Clicking it will trigger the scraping + summarization + data refresh for today.

How to enable locally:

1) Install deps and start the local API server

```
pip install -r requirements.txt
python server.py
```

2) Serve the site locally (avoid `file://` so CORS works)

```
python -m http.server 8000
```

3) Open http://localhost:8000 and use the button.

Notes:
- Requires `TOGETHER_API_KEY` or `GEMINI_API_KEY`/`GOOGLE_API_KEY` in your environment.
- The button is hidden when today already has papers, or when not running on localhost.
