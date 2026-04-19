# ReaDoc — AI-Powered Document Intelligence (RAG System)

ReaDoc is a full-stack **Retrieval-Augmented Generation (RAG)** application that allows users to upload documents (PDFs) and ask questions about them. The system retrieves relevant context using vector search and generates accurate answers using an LLM.

---

##  Live Features

* 📄 Upload PDF documents
* 🔍 Semantic search using vector embeddings
* 🤖 AI-generated answers using Groq LLM
* 📚 Source-backed responses (page + text chunks)
* 🌐 Clean responsive frontend (desktop + mobile)
* ⚡ FastAPI backend with async endpoints

---

##  Architecture

```text
User Query
   ↓
Embedding Model (Sentence Transformers)
   ↓
FAISS Vector Search
   ↓
Top-K Relevant Chunks
   ↓
LLM (Groq)
   ↓
Final Answer + Sources
```

---

##  Tech Stack

### Backend

* FastAPI
* FAISS (Vector Database)
* Sentence Transformers (`all-MiniLM-L6-v2`)
* PyMuPDF (PDF parsing)
* Groq API (LLM inference)

### Frontend

* HTML + Tailwind CSS
* Vanilla JavaScript (Fetch API)

---

##  Project Structure

```text
rag_project/
│
├── main.py                  # FastAPI app
├── requirements.txt
├── .env                     # API keys (not committed)
│
├── rag/
│   ├── pdf_loader.py        # PDF text extraction
│   ├── chunker.py           # Text chunking
│   ├── embedder.py          # Embedding generation
│   ├── generator.py         # Groq LLM integration
│
├── vector_store/
│   ├── faiss_store.py       # FAISS indexing + search
│
├── frontend/
│   ├── index.html           # Main UI (responsive)
│   ├── mobile.html          # (optional / legacy)
│
└── data/
    ├── uploads/             # Uploaded files
```

---

##  Setup Instructions

### 1. Clone Repo

```bash
git clone https://github.com/your-username/readoc.git
cd readoc
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add Environment Variables

Create `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

### 5. Run Server

```bash
uvicorn main:app --reload
```

---

### 6. Open App

```text
http://127.0.0.1:8000
```

---

##  API Endpoints

### Upload Document

```http
POST /upload
```

**Body:** FormData

* `file`: PDF file

---

### Query Document

```http
POST /query
```

**Body:**

```json
{
  "query": "What is machine learning?"
}
```

**Response:**

```json
{
  "query": "...",
  "answer": "...",
  "sources": [
    { "page": 2, "text": "..." }
  ]
}
```

---

## Example Workflow

1. Upload a PDF
2. Ask a question
3. System retrieves relevant chunks
4. LLM generates answer
5. Sources are displayed

---

##  Security Notes

* CORS restricted to frontend origin (no wildcard access)
* API keys stored in `.env`
* File uploads handled safely via FastAPI

---

##  Deployment

### Recommended Platforms:

* Render (free tier, auto-sleep)
* Railway (faster, usage-based)

---

##  Future Improvements

* DOCX support
* Streaming responses
* Chat history
* Better chunk ranking
* Authentication system

---

##  Author

Built as a full-stack AI project demonstrating:

* RAG pipeline design
* Vector search (FAISS)
* LLM integration (Groq)
* API + frontend integration

---

##  License

MIT License
