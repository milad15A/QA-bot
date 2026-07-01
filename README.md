# QA Bot

An intelligent Retrieval-Augmented Generation (RAG) assistant that answers user questions based on information extracted from PDF documents.

## Features

* PDF document ingestion
* Document chunking
* Embedding generation using Ollama embeddings
* FAISS vector database
* Semantic retrieval
* Question answering over private documents

## Tech Stack

* Python
* LangChain
* Ollama
* FAISS
* UV
* Gradio (planned)

## Project Structure

```text
QA-bot/
├── src/
│   └── app/
│       ├── ingestion/
│       ├── embeddings/
│       ├── retrieval/
│       └── vector_store/
├── scripts/
├── tests/
├── data/
├── pyproject.toml
└── README.md
```
## Workflow

Once documents have been processed and indexed into the vector database, the system enters the online inference phase. This workflow is executed every time a user asks a question.

```text
User
  ↓
GUI (FastAPI)
  ↓
User Query
  ↓
Query Validation
  ↓
Load FAISS Vector Store
  ↓
Retriever (Similarity Search)
  ↓
Top-K Relevant Chunks
  ↓
Prompt Construction
  ↓
LLM (AI Model)
  ↓
Generated Answer
  ↓
Display Answer in GUI
```

## Installation

```bash
git clone <repository-url>
cd QA-bot

uv venv
uv sync
```


## Run Document Ingestion

```bash
uv run python scripts/ingest_documents.py
```

## Current Status

* [x] Project setup
* [x] Logging system
* [x] PDF ingestion pipeline
* [x] FAISS integration
* [x] Retriever implementation
* [ ] QA chain
* [ ] User interface

# QA Bot

An intelligent Retrieval-Augmented Generation (RAG) assistant that answers user questions based on information extracted from PDF documents.

## Features

* PDF document ingestion
* Document chunking
* Embedding generation using Ollama embeddings
* FAISS vector database
* Semantic retrieval
* Question answering over private documents

## Tech Stack

* Python
* LangChain
* Ollama
* FAISS
* UV
* Gradio (planned)

## Project Structure

```text
QA-bot/
├── src/
│   └── app/
│       ├── ingestion/
│       ├── embeddings/
│       ├── retrieval/
│       └── vector_store/
├── scripts/
├── tests/
├── data/
├── pyproject.toml
└── README.md
```

## Installation

```bash
git clone <repository-url>
cd QA-bot

uv venv
uv sync
```

## Run Document Ingestion

```bash
uv run python scripts/ingest_documents.py
```

## Current Status

* [x] Project setup
* [x] Logging system
* [x] PDF ingestion pipeline
* [x] FAISS integration
* [x] Retriever implementation
* [ ] QA chain
* [ ] User interface

## Future Improvements

* OCR support for scanned PDFs
* Docker deployment
* CI/CD pipeline
* FastAPI backend
* Gradio web interface
## Engineering and MLOps Practices

This project is developed following software engineering and MLOps principles to ensure reproducibility, maintainability, and scalability.

Current practices include:

* Modular project architecture using a `src/` layout
* Dependency management with `uv` and `pyproject.toml`
* Version control with Git and GitHub
* Structured logging and input validation
* Separation of ingestion, retrieval, and serving components

Planned improvements:

* Containerization with Docker
* CI/CD pipelines using GitHub Actions
* Automated testing
* Configuration management
* Monitoring and observability

