# 📰 LATEST NEWS!

[![Plugin Version](https://img.shields.io/badge/version-1.0.5-blue)](https://github.com/matteocacciola/cat-latest-news)
[![Author](https://img.shields.io/badge/author-Andrea%20Pesce-green)](https://github.com/AndreaPesce2002)
[![Tags](https://img.shields.io/badge/tags-news%20%7C%20RSS-orange)]()

A plugin for [Grinning Cat](https://github.com/matteocacciola/grinning-cat-core) that lets the agent fetch and
summarise the **latest Italian news** from [RaiNews](https://www.rainews.it) — just ask in natural language.

---

## ✨ Features

| Feature             | Description                                                                   |
|---------------------|-------------------------------------------------------------------------------|
| 📡 Live RSS feed    | Pulls real-time news directly from the RaiNews RSS feeds                      |
| 🗂️ Topic filtering | Fetches news for specific topics or defaults to all categories                |
| 🔗 Source links     | Each news item includes its title, summary, publication date and original URL |
| 🧩 Zero config      | Drop in and go — no API keys or credentials required                          |

---

## 📦 Installation

Drop the `cat-latest-news` folder inside your plugins directory (by default `cat/plugins/`).
The plugin will be auto-discovered at startup.

```
cat/plugins/
└── cat-latest-news/
    ├── news.py
    ├── plugin.json
    ├── requirements.txt
    └── README.md
```

Install the Python dependency:

```bash
pip install feedparser>=6.0.10
```

Or let the Grinning Cat handle it automatically via `requirements.txt` on plugin load.

---

## 💬 Usage

Simply ask the Grinning Cat about the news in natural language. The agent will call the `latest_news` tool
automatically based on your request.

**Example prompts:**

```
What is the latest news in politics and economy?
Tell me today's sports and health headlines.
Give me the latest news on foreign affairs and technology.
```

---

## 🗂️ Available Categories

The following topics are supported. Multiple topics can be requested at once (comma-separated):

| Topic                          | Topic                |
|--------------------------------|----------------------|
| `politica`                     | `economia e finanza` |
| `scienza e tecnologia`         | `viaggi e turismo`   |
| `sport`                        | `cronaca`            |
| `stili di vita e tempo libero` | `salute`             |
| `arti e spettacolo`            | `societa`            |
| `esteri`                       | `economia`           |
| `inchieste`                    | `spettacolo`         |

> If the requested topics do not match any of the above, the plugin falls back to fetching news from **all** categories.

---

## 📋 Requirements

- [Grinning Cat Core](https://github.com/matteocacciola/grinning-cat-core)
- `feedparser >= 6.0.10`

---

## 👤 Author

**Andrea Pesce** — [github.com/AndreaPesce2002](https://github.com/AndreaPesce2002)
Adapted to Grinning Cat by **Matteo Cacciola** - [github.com/matteocacciola](https://github.com/matteocacciola)

Plugin repository: [github.com/matteocacciola/cat-latest-news](https://github.com/matteocacciola/cat-latest-news)
