
from app.retrieval.retriever import Retriever
from app.vectorstores.faiss_store import FAISSStore
from langchain_ollama import OllamaEmbeddings


def test_retriever():

    # 1. Load embeddings (must match ingestion!)
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    # 2. Load FAISS index
    db = FAISSStore.load("vector_store", embeddings)

    # 3. Create retriever
    retriever = Retriever(db)

    # 4. Test query
    query = "What is OEE?"

    results = retriever.retrieve(query)

    # 5. Print results
    for i, doc in enumerate(results):
        print(f"\n--- RESULT {i} ---")
        print(doc.page_content[:300])


if __name__ == "__main__":
    test_retriever()