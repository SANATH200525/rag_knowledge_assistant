from fastapi import FastAPI, UploadFile, File
import shutil
import uuid
from rag.pdf_loader import extract_text_by_page
from rag.chunker import chunk_text
from rag.embedder import embed_chunks
from vector_store.faiss_store import add_chunks_to_index,index


app = FastAPI()

@app.get("/")
def home():
    return {"message": "RAG Knowledge Assistant API"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    unique_id = uuid.uuid4()
    file_path = f"uploads/{unique_id}_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    pages = extract_text_by_page(file_path)

    chunks = chunk_text(pages)

    chunks = embed_chunks(chunks)
    #chunks = embed_chunks(chunks)

    add_chunks_to_index(chunks)

    return {
    "message": "Document indexed successfully",
    "document_id": str(unique_id),
    "pages": len(pages),
    "chunks": len(chunks),
    "vector_count": index.ntotal
    }