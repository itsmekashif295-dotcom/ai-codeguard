import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
DB_PATH = "rag_db"
client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_or_create_collection(name="cwe_knowledge")

def seed_database():
    docs = [
        "CWE-78: Command Injection. Fix: use subprocess.run with shell=False.",
        "CWE-89: SQL Injection. Fix: use parameterized queries or ORM.",
        "CWE-22: Path Traversal. Fix: validate and sanitize file paths.",
        "CWE-798: Hardcoded Secrets. Fix: use environment variables.",
        "CWE-327: Weak Crypto. Fix: use bcrypt or argon2."
    ]
    if collection.count() == 0:
        embeddings = model.encode(docs).tolist()
        collection.add(ids=[f"doc{i}" for i in range(len(docs))], documents=docs, embeddings=embeddings)

def get_cwe_context(cwe_id: str) -> str:
    if not cwe_id:
        return ""
    try:
        query_embedding = model.encode([cwe_id]).tolist()
        results = collection.query(query_embeddings=query_embedding, n_results=1)
        
        # Yahan hum string return kar rahe hain, dictionary nahi
        if results and 'documents' in results and len(results['documents']) > 0:
            if len(results['documents'][0]) > 0:
                return str(results['documents'][0][0])
    except Exception as e:
        print(f"RAG Error: {e}")
    return "No documentation found."