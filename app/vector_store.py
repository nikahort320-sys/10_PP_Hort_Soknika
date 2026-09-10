import chromadb
from app.config import CHROMA_DIR
from app.embeddings import get_embedding

def get_chroma_collection(collection_name="rag_documents"):
    client = chromadb.PersistentClient(path=CHROMA_DIR)
    return client.get_or_create_collection(name=collection_name)

def add_documents_to_vector_store(chunks, metadatas, ids):
    collection = get_chroma_collection()
    embeddings = [get_embedding(chunk) for chunk in chunks]
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )

def query_vector_store(query_text, top_k=3):
    collection = get_chroma_collection()
    query_vector = get_embedding(query_text)
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=top_k
    )
    return results["documents"][0], results["metadatas"][0]
