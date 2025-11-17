from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 1. Load HF embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# 2. Document list
docs = [
    "The Eiffel Tower is located in Paris.",
    "Python is a popular programming language.",
    "The sun is a star."
]

# 3. Embed documents
doc_emb = model.encode(docs)

# 4. Build FAISS index
dimension = doc_emb.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(doc_emb))

# 5. Query
query = "Where is the Eiffel Tower?"
query_emb = model.encode([query])

# 6. Retrieve top document
k = 1
dist, idx = index.search(query_emb, k)

print("Top result:", docs[idx[0][0]])

