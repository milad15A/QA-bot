from langchain_community.vectorstores import FAISS


class FAISSStore:

    @staticmethod
    def build(documents, embeddings):

        return FAISS.from_documents(
            documents,
            embeddings
        )

    @staticmethod
    def save(db, path: str):

        db.save_local(path)

    @staticmethod
    def load(path, embeddings):

        return FAISS.load_local(
            path,
            embeddings,
            allow_dangerous_deserialization=True,
        )