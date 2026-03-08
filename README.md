# RAG Knowledge Assistant

A Retrieval-Augmented Generation (RAG) backend built with FastAPI that allows semantic search over uploaded PDF documents.

The system processes documents, converts them into embeddings, and stores them in a FAISS vector index for efficient similarity search.

## Architecture

PDF Upload
→ Text Extraction
→ Chunking
→ Embedding Generation
→ FAISS Vector Index
→ Semantic Retrieval

## Tech Stack

Backend

* FastAPI

Document Processing

* PyMuPDF

Embeddings

* Sentence Transformers (all-MiniLM-L6-v2)

Vector Database

* FAISS

## Project Structure

rag_knowledge_assistant/

main.py
rag/
 pdf_loader.py
 chunker.py
 embedder.py

vector_store/
 faiss_store.py

uploads/

## Features Implemented

* PDF upload API
* Text extraction from PDFs
* Document chunking
* Embedding generation
* Vector indexing using FAISS

## Installation

Clone the repository

```
git clone <repo_url>
cd rag_knowledge_assistant
```

Create virtual environment

```
python -m venv venv
```

Activate virtual environment

Windows

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

## Run the Server

```
uvicorn main:app --reload
```

Open API docs

```
http://127.0.0.1:8000/docs
```

## API Endpoints

### Upload Document

POST /upload

Uploads and indexes a PDF document.

Response example

```
{
 "message": "Document indexed successfully",
 "document_id": "...",
 "pages": 3,
 "chunks": 8,
 "vector_count": 8
}
```

## Next Steps

* Semantic retrieval endpoint
* LLM integration
* Source citation
* FAISS persistence
* Frontend interface
* Deployment
