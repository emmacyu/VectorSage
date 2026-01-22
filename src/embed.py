from langchain.embeddings.base import Embeddings
from sentence_transformers import SentenceTransformer
from config import EMBED_MODEL


class HFEmbeddings(Embeddings):
    """LangChain Embeddings wrapper using sentence-transformers"""

    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts):
        return self.model.encode(texts, convert_to_numpy=True).tolist()

    def embed_query(self, text):
        return self.model.encode([text], convert_to_numpy=True)[0].tolist()
