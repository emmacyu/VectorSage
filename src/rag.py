from db import retrieve
from llm import generate
from config import MAX_CONTEXT_CHARS, TOP_K


def build_prompt(context: str, question: str) -> str:
    """
    English prompt, instruct the model to only answer based on the provided documents.
    """
    return f"""
You are a helpful assistant that answers questions **only using the provided documents**.

Document content:
{context}

Question:
{question}

Rules:
- Only use information from the documents.
- Do not make up any information.
- If the answer is not found in the documents, reply "No relevant information found."
- Answer in English.
"""


def rag_answer(question: str) -> str:
    # 1. match documents
    docs = retrieve(question, k=TOP_K)

    # 2. construct context
    context = "\n\n".join(docs)[:MAX_CONTEXT_CHARS]

    # 3. construct prompt
    prompt = build_prompt(context, question)

    # 4. LLM generate
    answer = generate(prompt)
    return answer


if __name__ == "__main__":
    question = "what is VectorSage?"
    answer = rag_answer(question)
    print("\n===== Answer =====")
    print(answer)
