import sys
from app.pipeline import run_rag_pipeline

def run_cli():
    print("==================================================")
    print(" Welcome to the Modular RAG CLI Application!")
    print(" Type 'exit' or 'quit' to end the session.")
    print("==================================================\n")
    
    while True:
        try:
            user_query = input("\nEnter your question: ").strip()
            if not user_query:
                continue
            if user_query.lower() in ["exit", "quit"]:
                print("Exiting RAG system. Goodbye!")
                break
            
            print("\nProcessing question through RAG pipeline...")
            answer, sources, chunks = run_rag_pipeline(user_query)
            
            print(f"Retrieved {len(chunks)} chunks from: {', '.join(sources)}")
            print("\n" + "="*50)
            print("ANSWER:")
            print("="*50)
            print(answer)
            print("="*50)
            
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cli()
