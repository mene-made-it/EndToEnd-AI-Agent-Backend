import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ========= LOAD PDF ========== #
print(f"Current dir: {os.getcwd()}")
pdf_path = "../../data/documents/mbase.pdf"
if not os.path.exists(pdf_path):
    raise FileNotFoundError(f"PDF File not found: {pdf_path}")

pdf_loader = PyPDFLoader(pdf_path)
try:
    pages = pdf_loader.load()
    print(f"PDF has been loaded and has {len(pages)} pages")

except Exception as e:
    print(f"Error loading PDF: {e}")
    raise


# ===== CHUNK ====== #
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

pages_split = text_splitter.split_documents(pages)



