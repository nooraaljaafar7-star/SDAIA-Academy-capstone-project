Markdown
# 📑 Automated Contract Audit & Vendor Compliance Pipeline

An end-to-end AI-powered legal & security audit framework designed to evaluate contract compliance against internal organization policies. Built using **Groq (LLaMA 3.3 70B)**, **ChromaDB (RAG)**, **FastAPI**, and **Gradio**.

---

## 📌 Features

* 📄 **PDF Contract Processing**: Automated extraction and structure parsing from uploaded vendor contracts using `PyPDF`.
* 🔍 **Policy Retrieval Augmented Generation (RAG)**: Vector similarity matching powered by `ChromaDB` and HuggingFace embeddings (`all-MiniLM-L6-v2`) to pull exact governance rules.
* 🧠 **LLM Compliance Engine**: Fast, structured analysis using **Groq's LLaMA 3.3 70B** model to output accurate risk levels, rationale, and actionable remediation steps.
* 📊 **Metrics Tracking**: Real-time reporting on execution latency and operational costs.
* 🖥️ **Interactive UI & REST API**: Features a **Gradio** web interface for end-users and a **FastAPI** backend for programmatic integrations.
* 🐳 **Docker Ready**: Fully containerized setup for seamless, reproducible deployment.

---

graph TD
    A[📄 PDF Contract] --> B[🔍 Text Extraction]
    B --> C[🗂️ ChromaDB - RAG Rules Query]
    C --> D[🧠 Groq LLaMA 3.3 70B Engine]
    D --> E[📊 Structured JSON Audit Report]
---

## 🚀 Quick Start (Docker Deployment)

The easiest way to run the application is using Docker Compose.

### Prerequisites

* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
* A valid **Groq API Key**.

### Steps

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/nooraaljaafar7-star/SDAIA-Academy-capstone-project.git](https://github.com/nooraaljaafar7-star/SDAIA-Academy-capstone-project.git)
   cd SDAIA-Academy-capstone-project
Set up Environment Variables:
Create a .env file in the root directory:

Code snippet
GROQ_API_KEY=gsk_your_groq_api_key_here
Run using Docker Compose:

Bash
docker-compose up -d
Access the Interfaces:

Gradio Web Interface: http://localhost:7860

FastAPI Docs (Swagger): http://localhost:8000/docs

🛑 Stopping the Container
To stop and remove running containers:

Bash
docker-compose down
## 🏛️ Organization & Acknowledgments

This project was developed as part of the capstone requirements for <a href="https://github.com/SDAIAAcademy" target="_blank">SDAIA Academy</a>.

* **Organization:** <a href="https://github.com/SDAIAAcademy" target="_blank">SDAIA Academy</a>
