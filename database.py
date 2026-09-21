import lancedb
from sentence_transformers import SentenceTransformer
from parser import load_and_chunk_codebase

# Local Embedding Model (Fast & Offline)
print("⏳ Embedding model load ho raha hai...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Local LanceDB Connection
db = lancedb.connect("./codevault_db")


def index_codebase(repo_path="."):
    """Code chunks ko embed karke LanceDB mein index karta hai."""
    print("🔍 Codebase parsing shuru...")
    raw_chunks = load_and_chunk_codebase(repo_path)

    if not raw_chunks:
        print("⚠️ Koi valid code chunks nahi mile!")
        return None

    print(f"⚡ {len(raw_chunks)} chunks ke liye embeddings generate ho rahe hain...")

    data = []
    contents = [c["content"] for c in raw_chunks]
    embeddings = model.encode(contents, show_progress_bar=True)

    for idx, chunk in enumerate(raw_chunks):
        data.append(
            {
                "vector": embeddings[idx].tolist(),
                "text": chunk["content"],
                "file": chunk["file"],
                "start_line": chunk["start_line"],
                "end_line": chunk["end_line"],
            }
        )

    # LanceDB table create / overwrite
    table = db.create_table("code_vectors", data=data, mode="overwrite")
    print("✅ LanceDB indexing complete ho gayi!")
    return table


def search_code(query, top_k=3):
    """User query ke basis par relevant code chunks dhoondhta hai."""
    table = db.open_table("code_vectors")
    query_vector = model.encode(query).tolist()
    results = table.search(query_vector).limit(top_k).to_list()
    return results


if __name__ == "__main__":
    # Indexing Test
    index_codebase(".")

    # Search Test
    print("\n🔎 Testing Semantic Search:")
    test_query = "chunk size for code"
    matches = search_code(test_query)

    for i, res in enumerate(matches, 1):
        print(f"\n--- Result {i} (File: {res['file']}) ---")
        print(f"Lines: {res['start_line']}-{res['end_line']}")
        print(f"Snippet:\n{res['text'][:120]}...")