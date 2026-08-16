<div align="center">

# 📊 csv-chat-local

**Chat with your CSV files locally using Streamlit and OpenAI. 100% open source.**

[![PyPI version](https://badge.fury.io/py/csv-chat-local.svg)](https://badge.fury.io/py/csv-chat-local)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/varungor365/csv-chat-local/actions/workflows/ci.yml/badge.svg)](https://github.com/varungor365/csv-chat-local/actions)

<br/>

</div>

---

## ✨ Why this exists

Data analysis can be tedious. Instead of writing `pandas` queries manually, what if you could just ask your data questions?

**csv-chat-local** provides a beautiful, local web interface to upload any CSV file and chat with it. It uses `PandasAI` under the hood to write and execute python code on the fly to answer your questions.

### Features
- 🗣️ **Natural Language:** Ask "What were the total sales in Q3?" instead of writing `.groupby()`.
- 📊 **Beautiful UI:** Built with Streamlit for a responsive, clean chat interface.
- 🔒 **BYOK (Bring Your Own Key):** Just drop in your OpenAI API key in the sidebar.

---

## 🚀 Quickstart

### Install
```bash
pip install csv-chat-local
```

### Run
```bash
csv-chat
```
This will automatically launch the Streamlit app in your default browser at `http://localhost:8501`.

---

## 🤖 AI Agent Context

See [CLAUDE.md](CLAUDE.md) for contribution guidelines.

---

## 📄 License

MIT © Varun Ruhella. See [LICENSE](LICENSE) for details.

## Who this is for

CSV Chat Local lets you explore tabular data through a local Streamlit interface and an LLM workflow. It is useful for analysts, students, and developers who want to ask questions about CSV files without turning the repository into a hosted data service.

## Why star this repository

Star this project if local data analysis, CSV exploration, Streamlit, or privacy-conscious LLM workflows are useful to you.
