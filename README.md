# What is happening in this project

## Naive RAG Chatbot  
  ChromaDB + Groq + Streamlit*



This is a simple RAG (Retrieval-Augmented Generation) chatbot  
 I built this to understand how vector databases actually work in a real pipeline  
 it reads a PDF → chunks it → stores it in ChromaDB → retrieves relevant bits → sends to LLM → profit  > also — it has full conversation memory, so it actually remembers what you said earlier 


  ## Folder Structure
sepration/
│
├── Ingestion.py      ← reads the PDF, splits into chunks, stores into ChromaDB
├── retrival.py       ← takes a user query, searches ChromaDB, returns top result
├── generation.py     ← streamlit UI + Groq API + context-aware chat
├── .env              ← your API key goes here (NOT pushed to GitHub)
├── .env.example      ← template showing what keys are needed
├── requirements.txt  ← all dependencies
└── .gitignore        ← keeps secrets & local data out of git


#  how this project wroks

PDF
 │
 ▼
[Ingestion.py]
 │  - reads all pages using PyPDF2
 │  - splits text into 500-char chunks
 │  - stores chunks into ChromaDB (persistent, saved to ./db)
 ▼
ChromaDB (vector store on disk)
 │
 ▼
[retrival.py]   ← called when user asks something
 │  - takes the user's question
 │  - queries ChromaDB for the most relevant chunk
 │  - returns that chunk as "context"
 ▼
[generation.py]  ← the main streamlit app
 │  - shows a chat UI
 │  - builds prompt: system prompt (doc context) + full chat history
 │  - sends everything to Groq (llama-3.1-8b-instant)
 │  - displays the answer + remembers it for next turn


# setup & install

**1. Clone the repo**
git clone <your-repo-url>  
cd sepration

**2. Install dependencies**

pip install -r requirements.txt


**3. Set up your API key**

# copy the example file
cp .env.example .env

# then open .env and paste your Groq API key
GROQ_API_KEY=your_groq_api_key_here

> Get your free Groq API key at → https://console.groq.com





# how to run

**Step 1 — Ingest your PDF first (only once)**

python Ingestion.py

> chunks the PDF and saves to `./db`

**Step 2 — Launch the chatbot**

python -m streamlit run generation.py

> opens in browser at → `http://localhost:8501`



