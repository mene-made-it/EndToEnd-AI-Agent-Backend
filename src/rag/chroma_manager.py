import os
from langchain_chroma import Chroma
from src.rag.data_loader import pages_split
from src.rag.embeddings import embeddings

persist_directory = r"C:\Users\gianl\PycharmProjects\EndToEnd-AI-Agent\data\vectordb"
collection_name = "math"


if not os.path.exists(persist_directory):
    os.makedirs(persist_directory)

try:
    vectorstore = Chroma.from_documents(
        documents=pages_split,
        embedding=embeddings,
        persist_directory=persist_directory,
        collection_name=collection_name
    )
    print(f"Created ChromaDB vector store!")

except Exception as e:
    print(f"Error setting up ChromaDB: {str(e)}")
    raise


retriever = vectorstore.as_retriever(
    search_type = "similarity",
    search_kwargs = {"k": 5} # k = num to chunks to return
)
