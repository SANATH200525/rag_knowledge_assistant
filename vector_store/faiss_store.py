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