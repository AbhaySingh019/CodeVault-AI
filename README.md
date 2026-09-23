# 🔒 CodeVault-AI

> **100% Offline, Privacy-Focused On-Device Code Intelligence & Security Audit Engine**

CodeVault-AI is an air-gapped, high-performance developer companion designed for Qualcomm Snapdragon-powered devices. It provides local semantic code search, automated architectural security auditing, and code intelligence without exposing sensitive enterprise codebases to the cloud.

---

## ⚡ Core Value Proposition

* **100% On-Device & Privacy-First:** Zero data leaves your machine. Fully operational in air-gapped environments.
* **Hardware-Accelerated Performance:** Optimized using ONNX Runtime for local Snapdragon NPU execution.
* **Sub-Second Code Retrieval:** Powered by LanceDB for ultra-fast local vector search.
* **AST-Aware Chunking:** Uses Tree-sitter parsing for context-aware code analysis across multi-language projects.

---

## 🛠️ Tech Stack

* **Core Runtime:** Python 3.11+
* **Parsing Engine:** Tree-sitter
* **Vector Store:** LanceDB (Embedded Vector Database)
* **Embeddings:** Sentence-Transformers (`all-MiniLM-L6-v2`)
* **Inference Engine:** ONNX Runtime (NPU Acceleration)
* **Backend Framework:** FastAPI & Uvicorn
* **Frontend UI:** Streamlit

---

## 🚀 Quick Start & Local Setup

### Prerequisites
* Windows 11 (Snapdragon / ARM64 or x86_64)
* Python 3.10 or higher
* Git

### Installation

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/AbhaySingh019/CodeVault-AI.git](https://github.com/AbhaySingh019/CodeVault-AI.git)
   cd CodeVault-AI
