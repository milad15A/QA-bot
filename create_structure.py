from pathlib import Path

structure = [
    ".github/workflows",
    "app/api",
    "app/core",
    "app/llms",
    "app/retrieval",
    "app/pipelines",
    "app/services",
    "data/raw",
    "data/processed",
    "vector_store",
    "scripts",
    "tests/unit",
    "tests/integration",
    "notebooks",
    "deployment/kubernetes",
    "docs"
]

files = [
    ".github/workflows/ci.yml",
    ".github/workflows/cd.yml",

    "app/api/__init__.py",
    "app/api/routes.py",
    "app/api/schemas.py",

    "app/core/__init__.py",
    "app/core/config.py",
    "app/core/logger.py",
    "app/core/exceptions.py",

    "app/llms/__init__.py",
    "app/llms/factory.py",
    "app/llms/prompts.py",

    "app/retrieval/__init__.py",
    "app/retrieval/embeddings.py",
    "app/retrieval/vector_store.py",
    "app/retrieval/retriever.py",
    "app/retrieval/reranker.py",

    "app/pipelines/__init__.py",
    "app/pipelines/rag_pipeline.py",

    "app/services/__init__.py",
    "app/services/qa_service.py",

    "app/main.py",

    "scripts/ingest_documents.py",
    "scripts/build_index.py",
    "scripts/evaluate_rag.py",

    "tests/conftest.py",
    "tests/unit/test_llm.py",
    "tests/unit/test_retriever.py",
    "tests/unit/test_pipeline.py",
    "tests/integration/test_api.py",

    "docs/architecture.md",
    "docs/api.md",

    ".env.example",
    ".gitignore",
    ".dockerignore",
    ".pre-commit-config.yaml",
    "pyproject.toml",
    "README.md",
    "Makefile",
    "LICENSE",

    "deployment/Dockerfile",
    "deployment/docker-compose.yml",
    "deployment/kubernetes/deployment.yaml",
    "deployment/kubernetes/service.yaml",
]

root = Path(".")

for folder in structure:
    (root / folder).mkdir(parents=True, exist_ok=True)

for file in files:
    path = root / file
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)

print("Project structure created successfully.")