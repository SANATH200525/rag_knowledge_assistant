from fastapi import FastAPI, UploadFile, File,Body
import shutil
import uuid
from rag.pdf_loader import extract_text_by_page
from rag.chunker import chunk_text
from rag.embedder import embed_chunks,embed_query
from vector_store.faiss_store import add_chunks_to_index,index,search
from pydantic import BaseModel
from rag.generator import generate_answer
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from fastapi.responses import FileResponse



class QueryRequest(BaseModel):
    query: str
app = FastAPI()
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def serve_home():
    return FileResponse("frontend/index.html")

@app.get("/health")
def check_health():
    return {"status":"ok"}


from fastapi import FastAPI, UploadFile, File, Request, HTTPException, status
import uuid
import shutil
import os

# Set limit to 10 MB (in bytes)
MAX_FILE_SIZE = 10 * 1024 * 1024  

@app.post("/upload")
async def upload_pdf(request: Request, file: UploadFile = File(...)):
    # 1. File Size Validation
    content_length = request.headers.get('content-length')
    if content_length and int(content_length) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, 
            detail=f"File too large. Maximum size is {MAX_FILE_SIZE / (1024 * 1024)} MB."
        )

    # 2. Ensure uploads directory exists
    os.makedirs("uploads", exist_ok=True)

    # 3. Save the uploaded file
    unique_id = uuid.uuid4()
    file_path = f"uploads/{unique_id}_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 4. Process the document
    try:
        pages = extract_text_by_page(file_path)
        chunks = chunk_text(pages)
        chunks = embed_chunks(chunks)
        add_chunks_to_index(chunks)
        
    except Exception as e:
        # If parsing or embedding crashes (like an Out of Memory error), 
        # delete the file so it doesn't waste limited server storage.
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(status_code=500, detail=f"Error processing document: {str(e)}")

    # 5. Return Success
    return {
        "message": "Document indexed successfully",
        "document_id": str(unique_id),
        "pages": len(pages),
        "chunks": len(chunks),
        "vector_count": index.ntotal
    }
    
    
@app.post("/query")
async def query_document(request: QueryRequest):

    query = request.query

    query_embedding = embed_query(query)

    results = search(query_embedding, k=5)
    answer = generate_answer(query, results)


    return {
        "query": query,
        "answer": answer,
        "sources": results
    }