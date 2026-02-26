import chromadb
from PyPDF2 import PdfReader

chroma_client = chromadb.PersistentClient(path="./db")
collection = chroma_client.get_or_create_collection(name="my-collection")

reader = PdfReader(r"D:\Noman Bhai AI\VectordB\ariticle\Reinforcement_Learning_Advancements_Limitations_an.pdf")
full_text = ""
for page in reader.pages:
    text = page.extract_text()
    if text:
        full_text += text + "\n"

CHUNK_SIZE = 200
chunks = [] 


for i in range(0, len(full_text), CHUNK_SIZE):
    

    chunk_piece = full_text[i : i + CHUNK_SIZE]
   
    chunks.append(chunk_piece)

chunk_ids = [f"chunk_{i}" for i in range(len(chunks))]

print(f"Adding {len(chunks)} chunks to ChromaDB (please wait babe......)...")
collection.add(
    ids=chunk_ids,
    documents=chunks
)
print("Done.Ingestion complete")