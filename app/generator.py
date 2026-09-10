import ollama
from app.config import LLM_MODEL

def generate_answer(query: str, context_chunks: list) -> str:
    context_str = "\n\n".join(context_chunks)
    
    prompt = f"""You are a helpful assistant. Answer the user's question using ONLY the provided context below. If the answer cannot be found in the context, state that you do not have enough information.

Context:
{context_str}

Question:
{query}

Answer:"""

    response = ollama.generate(
        model=LLM_MODEL,
        prompt=prompt
    )
    
    return response["response"]
