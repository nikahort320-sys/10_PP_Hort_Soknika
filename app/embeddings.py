import ollama
from app.config import EMBEDDING_MODEL

def get_embedding(text: str) -> list:
    response = ollama.embeddings(model=EMBEDDING_MODEL, prompt=text)
    return response["embedding"]
