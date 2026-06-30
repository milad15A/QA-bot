from langchain_community.vectorstores import FAISS
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_ollama import ChatOllama
from app.core.logger import get_logger


logger = get_logger(__name__)



class Retriever:

    def __init__(self, db: FAISS):
        self.db = db

        logger.info("Initializing MultiQueryRetriever with Llama3")

        llm = ChatOllama(model="llama3.1")

        self.retriever = MultiQueryRetriever.from_llm(
            retriever=db.as_retriever(search_kwargs={"k": 3}),
            llm=llm
        )

        logger.info("Retriever initialized successfully")

    def retrieve(self, query: str):
        logger.info(f"User query received: {query}")

        results = self.retriever.invoke(query)

        logger.info(f"Retrieved {len(results)} documents")

        return results
        