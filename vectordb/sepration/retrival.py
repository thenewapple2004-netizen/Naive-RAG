import chromadb

def get_context(user_query):
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    collection = chroma_client.get_or_create_collection(name="my-collection")

    context = collection.query(
        query_texts=[user_query],
        n_results=1
    )
    return "\n".join(context["documents"][0])