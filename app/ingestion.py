import os
import glob
from app.config import DATA_DIR, CHUNK_SIZE, CHUNK_OVERLAP
from app.vector_store import add_documents_to_vector_store

def load_documents():
    documents = []
    files = glob.glob(os.path.join(DATA_DIR, "*.txt")) + glob.glob(os.path.join(DATA_DIR, "*.md"))
    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            documents.append({"file_name": os.path.basename(file_path), "text": content})
    print(f"[Ingestion] Loaded {len(documents)} document(s) from '{DATA_DIR}'.")
    return documents

def split_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def run_ingestion():
    docs = load_documents()
    all_chunks, all_metadatas, all_ids = [], [], []
    
    doc_id = 0
    for doc in docs:
        chunks = split_text(doc["text"])
        for chunk in chunks:
            all_chunks.append(chunk)
            all_metadatas.append({"source": doc["file_name"]})
            all_ids.append(f"doc_{doc_id}")
            doc_id += 1
            
    add_documents_to_vector_store(all_chunks, all_metadatas, all_ids)
    print(f"[VectorStore] Successfully ingested {doc_id} chunks into ChromaDB.")

if __name__ == "__main__":
    run_ingestion()
