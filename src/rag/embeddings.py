from langchain_huggingface import HuggingFaceEmbeddings


# make sure is compatible embedding and model
embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

