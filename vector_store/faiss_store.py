import faiss
import numpy as np

# embedding dimension for MiniLM
DIMENSION = 384

# create FAISS index
index = faiss.IndexFlatL2(DIMENSION)

# metadata store
metadata_store = {}

def add_chunks_to_index(chunks):

    vectors = []
    ids = []

    start_id = len(metadata_store)

    for i, chunk in enumerate(chunks):

        vector_id = start_id + i

        vectors.append(chunk["embedding"])
        ids.append(vector_id)

        metadata_store[vector_id] = {
            "text": chunk["text"],
            "page": chunk["page"]
        }

    vectors = np.array(vectors).astype("float32")

    index.add(vectors)
    
    
def search(query_embedding, k=5):
    import numpy as np

    query_vector = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_vector, k)

    results = []

    for i in indices[0]:
        if i in metadata_store:
            results.append(metadata_store[i])

    return results