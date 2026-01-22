from pymongo import MongoClient
import numpy as np
from embed import HFEmbeddings
from config import MONGO_URI, DB_NAME, COLLECTION_NAME, TOP_K

client = MongoClient(MONGO_URI)
col = client[DB_NAME][COLLECTION_NAME]
embeddings = HFEmbeddings()


def insert_documents(docs):
    """docs = [{'text': ..., 'metadata': {...}}, ...]"""
    for doc in docs:
        doc["vector"] = embeddings.embed_query(doc["text"])
    col.insert_many(docs)


def retrieve(query, k=TOP_K):
    query_vec = embeddings.embed_query(query)
    docs = list(col.find())
    scores = []
    for d in docs:
        vec = np.array(d["vector"])
        score = np.dot(vec, query_vec) / (np.linalg.norm(vec) * np.linalg.norm(query_vec))
        scores.append((score, d["text"]))
    scores.sort(reverse=True, key=lambda x: x[0])
    return [t[1] for t in scores[:k]]
