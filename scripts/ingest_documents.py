from app.ingestion.pdf_loader import PDFLoader
from app.ingestion.text_splitter import DocumentSplitter
from app.embeddings.embedding_factory import EmbeddingFactory   
from app.vectorstores.faiss_store import FAISSStore
from app.core.logger import get_logger    
logger = get_logger(__name__)

def main(
    pdf_path: str ="data/raw/sample.pdf",
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
    embedding_model: str = "nomic-embed-text"
):

    logger.info(f"Loading PDF: {pdf_path}")

    documents = PDFLoader.load(pdf_path)

    logger.info(f"Loaded {len(documents)} pages")

    splitter = DocumentSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split(documents)

    logger.info(f"Created {len(chunks)} chunks")

    embeddings = EmbeddingFactory.create(
        model_name=embedding_model
    )

    logger.info("Embedding model created")

    db = FAISSStore.build(chunks, embeddings)

    logger.info("FAISS index built")

    FAISSStore.save(db, "vector_store")

    logger.info("FAISS index saved successfully")

    return db

if __name__ == "__main__":
    main()