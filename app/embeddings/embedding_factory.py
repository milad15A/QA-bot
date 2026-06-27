from langchain_ollama import OllamaEmbeddings


class EmbeddingFactory:

    @staticmethod
    def create(
        model_name: str = "nomic-embed-text",
    ):

        return OllamaEmbeddings(
            model=model_name
        )