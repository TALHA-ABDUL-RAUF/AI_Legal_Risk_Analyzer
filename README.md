
<div align="center">

<br/>

> I built this because reading a 40-page NDA at 1am shouldn't feel like defusing a bomb. Upload the contract, ask what you actually want to know ("can they terminate this without notice?"), and get an answer grounded in the actual clauses — not a guess.

<br/>

## 📖 Table of Contents

<details>
<summary>Click to expand</summary>

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Sample Documents](#-sample-documents)
- [Roadmap](#-roadmap)
- [Author](#-author)

</details>

<br/>

## 🧠 Overview

**AI Legal Risk Analyzer** is a Retrieval-Augmented Generation (RAG) system for contract review. It doesn't just summarize documents — it retrieves the *exact* clauses relevant to your question, then asks a local LLM to reason strictly over that retrieved text, flagging risk level, potential exposure, and recommendations.

Everything — embeddings, vector search, and inference — runs **locally via Ollama**. No contract text, no questions, no data ever hits an external API.

<br/>

## ✨ Features

<table>
<tr>
<td width="33%" valign="top">

<br/>

## 🛠 Tech Stack

<div align="center">

<br/>

## 🔄 How It Works

```mermaid
flowchart LR
    A[📤 Upload] --> B[✅ Validate]
    B --> C[📄 Extract Text]
    C --> D[🧩 Chunk]
    D --> E[🧠 Embed]
    E --> F[(🗂️ ChromaDB)]
    F --> G[🔎 Semantic Search]
    G --> H[📑 Retrieve Clauses]
    H --> I[🦙 Llama3 Reasoning]
    I --> J[⚖️ Risk Report]
    J --> K[📥 PDF Export]

    style A fill:#1f2937,stroke:#6E56CF,color:#fff
    style K fill:#1f2937,stroke:#6E56CF,color:#fff
    style I fill:#6E56CF,stroke:#1f2937,color:#fff
```

<sub>Diagram renders on GitHub/GitLab. Fallback: Upload → Validate → Extract → Chunk → Embed → ChromaDB → Search → Retrieve → Llama3 → Risk Report → PDF</sub>

<br/>

## 📁 Project Structure

```
AI_Legal_Risk_Analyzer/
├── 🚀 app.py                  → Entry point
├── 🔐 auth/                   → Login & session handling
├── 🗄️ database/                → Models, CRUD, DB session
├── ⚙️ services/                → Embeddings, vector store, search, LLM analyzer
├── 🧰 utils/                   → PDF export & helpers
├── 🖥️ views/                   → Streamlit pages (dashboard, search, history)
├── 📤 uploads/                 → Uploaded contracts
├── 🧪 tests/                   → Test suite
├── 🖼️ screenshots/             → App screenshots
├── 📚 sample_documents/        → Example contracts to try
├── requirements.txt
└── README.md
```

<br/>

## ⚙️ Getting Started

```bash
# clone it
git clone https://github.com/USERNAME/AI_Legal_Risk_Analyzer.git
cd AI_Legal_Risk_Analyzer

# set up environment
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# install deps
pip install -r requirements.txt

# init db
python -m database.init_db

# pull the model (one-time)
ollama pull llama3:8b

# launch
streamlit run app.py
```

> ⚠️ **Prerequisite:** [Ollama](https://ollama.com/) must be installed and running locally before you start the app — the analyzer talks to it directly.

<br/>

## 📚 Sample Documents

Not ready to upload your own NDA at 2am? Grab one from [`sample_documents/`](./sample_documents) and test the full pipeline in minutes.

<br/>

## 🚀 Roadmap

- [ ] Multi-document cross-referencing
- [ ] OCR for scanned contracts
- [ ] Clause-level risk classification
- [ ] Visual risk-scoring dashboard
- [ ] Docker + cloud deployment
- [ ] JWT-based auth
- [ ] Multi-agent legal reasoning pipeline

<br/>

## 👤 Author

<div align="center">
