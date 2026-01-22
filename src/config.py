# config.py
LLM_MODEL_PATH = "/Users/Test/coding-projects/VectorSage/models/"
LLM_MODEL_NAME = "gpt4all-falcon.Q4_0"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "vector_db"
COLLECTION_NAME = "vectors"
DOC_FOLDER = "/Users/Test/coding-projects/VectorSage/docs"

# constraints
MAX_TOKENS = 512
TEMPERATURE = 0.1

# RAG
TOP_K = 4
MAX_CONTEXT_CHARS = 4000