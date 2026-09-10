import ollama

def test_ollama_setup():
    print("--- 1. Testing Generation Model (qwen3:8b) ---")
    try:
        gen_response = ollama.generate(
            model="qwen3:8b", 
            prompt="Say 'Ollama qwen3 is working!'"
        )
        print(f"Response: {gen_response['response'].strip()}\n")
    except Exception as e:
        print(f"Generation error: {e}\n")

    print("--- 2. Testing Embedding Model (nomic-embed-text) ---")
    try:
        embed_response = ollama.embeddings(
            model="nomic-embed-text", 
            prompt="Testing embedding model."
        )
        vector = embed_response["embedding"]
        print(f"Success! Generated vector of dimension size: {len(vector)}")
    except Exception as e:
        print(f"Embedding error: {e}")

if __name__ == "__main__":
    test_ollama_setup()
