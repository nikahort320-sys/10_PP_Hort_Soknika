from app.retriever import retrieve_context
from app.generator import generate_answer

def run_rag_pipeline(query: str):
    chunks, metadatas = retrieve_context(query, top_k=3)
    sources = list(set(meta["source"] for meta in metadatas))
    answer = generate_answer(query, chunks)
    return answer, sources, chunks
