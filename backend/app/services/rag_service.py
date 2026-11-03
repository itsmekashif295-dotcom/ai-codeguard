import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.PersistentClient(path="./rag_db")
collection = client.get_or_create_collection(name="cwe_knowledge")

def seed_database():
    docs = [
        "CWE-78: Command Injection. User input is passed to os.system or subprocess with shell=True. Fix: use subprocess.run with shell=False and validate input.",
        "CWE-89: SQL Injection. User input is concatenated into SQL queries. Fix: use parameterized queries or ORM.",
        "CWE-22: Path Traversal. User input is used to build file paths. Fix: validate and sanitize file paths, use os.path.basename.",
        "CWE-798: Hardcoded Secrets. API keys or passwords are written directly in code. Fix: use environment variables or secret managers.",
        "CWE-327: Weak Crypto. Using MD5 or SHA1 for passwords. Fix: use bcrypt, argon2, or SHA-256 with salt."
    ]
    
    if collection.count() == 0:
        embeddings = model.encode(docs).tolist()
        collection.add(
            ids=[f"doc{i}" for i in range(len(docs))],
            documents=docs,
            embeddings=embeddings
        )
        print("Database seeded with CWE knowledge.")
    else:
        print("Database already has data.")

def retrieve_cwe(cwe_id: str) -> str:
    query_embedding = model.encode([cwe_id]).tolist()
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=1
    )
    if results['documents'] and results['documents'][0]:
        return results['documents'][0][0]
    return "No documentation found."