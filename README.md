🔒 CodeVault-AI

100% AI-Generated Project 🤖

This entire application—from architecture design, AST-aware parsing, vector search integration, local inference logic, FastAPI backend, and Streamlit dashboard—was designed, coded, and assembled 100% using AI.

📌 Project Overview

CodeVault-AI is a privacy-first, 100% offline-first local code intelligence and automated security auditing system. Built specifically for air-gapped environments and optimized for Snapdragon NPU hardware acceleration, CodeVault-AI enables software developers and security auditors to index, search, and analyze proprietary codebases locally without a single byte leaving the host machine.

✨ Key Features

🔒 100% Air-Gapped & Offline: Zero reliance on external cloud APIs or internet connectivity.

🌳 AST-Aware Code Chunking: Uses Tree-sitter AST parsing to extract full functions and classes instead of breaking code across arbitrary line limits.

⚡ Embedded Vector Search: Powered by LanceDB and Sentence-Transformers (all-MiniLM-L6-v2) for sub-second local semantic queries.

🛡️ Real-Time Security Audit: Automated static analysis rules detecting risks like eval(), exec(), hardcoded secrets, and unsafe subprocess execution.

🚀 Hardware Acceleration: Native ONNX Runtime support tuned for Snapdragon Hexagon NPU and local CPU/GPU execution providers.

🖥️ Microservices Architecture: Fully decoupled REST API (FastAPI) and interactive UI (Streamlit).

🏗️ Architecture & Data Flow

┌─────────────────────────────────────────────────────────────┐
│                    Streamlit Web UI (app.py)                │
└──────────────────────────────┬──────────────────────────────┘
                               │ HTTP REST Requests
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                   FastAPI Backend (main.py)                 │
└──────────────────────────────┬──────────────────────────────┘
                               │
               ┌───────────────┴───────────────┐
               ▼                               ▼
┌──────────────────────────────┐┌──────────────────────────────┐
│ Local DB & Embeddings        ││ Inference & Security Audit   │
│ (database.py / parser.py)    ││ (engine.py)                  │
│                              ││                              │
│ • AST-Aware Tree-Sitter      ││ • ONNX Execution Provider    │
│ • Sentence Transformers      ││ • Static Security Analysis   │
│ • Embedded LanceDB           ││ • Query Context Formatting   │
└──────────────────────────────┘└──────────────────────────────┘


🛠️ Tech Stack

Language: Python 3.10+

Code Parser: tree-sitter

Embeddings: sentence-transformers (all-MiniLM-L6-v2)

Vector DB: LanceDB

Inference Engine: ONNX Runtime

Backend Framework: FastAPI + Uvicorn

Frontend UI: Streamlit

🚀 Quick Start & Installation

1. Prerequisites & Virtual Environment

Ensure Python 3.10+ is installed on your system.

# Clone the repository
git clone https://github.com/your-username/CodeVault-AI.git
cd CodeVault-AI

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Install required dependencies
pip install -r requirements.txt


2. Running the Application

CodeVault-AI uses a dual-terminal split setup:

Terminal 1: FastAPI Backend Server

python main.py


Backend will run locally at http://127.0.0.1:8000

Terminal 2: Streamlit Frontend Dashboard

Open a new terminal tab, activate venv, and run:

streamlit run app.py


Frontend dashboard will launch in your default web browser at http://localhost:8501

🤖 AI Transparency Statement

This project, CodeVault-AI, was 100% conceptualized, designed, and developed using Artificial Intelligence.

Code Logic: All modules (parser.py, database.py, engine.py, main.py, app.py) were generated through collaborative AI prompts.

Architecture: The decoupled microservice model (FastAPI + Streamlit + LanceDB + ONNX) was architected by AI.

Documentation & Pitch Decks: All project briefs, presentation slides, and setup guides were compiled by AI.

📜 License

This project is released under the MIT License.
