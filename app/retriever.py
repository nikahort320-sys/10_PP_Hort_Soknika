from app.vector_store import query_vector_store

def retrieve_context(query: str, top_k: int = 3):
    chunks, metadatas = query_vector_store(query, top_k=top_k)
    return chunks, metadatas
