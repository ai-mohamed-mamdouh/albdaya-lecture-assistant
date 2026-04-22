# load docs and prepare to  store in vector db
from app.config import *
from langchain_core.documents import Document
from app.vector_store import get_vector_store

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_splite_docs(docs_path):
    # load data
    loader = PyPDFLoader( file_path=docs_path )
    docs = loader.load()

    # splitte to chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
        )
    chunks = splitter.split_documents(docs)
    
    return chunks

def save_lecture_chunks(chunks, lecture_name):
    vector_store = get_vector_store()

    docs = []
    ids = []

    for i, chunk in enumerate(chunks):
        docs.append(
            Document(
                page_content=chunk.page_content,
                metadata={
                    "lecture_name": lecture_name,
                    **chunk.metadata
                }
            )
        )
        ids.append(f"{lecture_name}_{i}")

    vector_store.add_documents(documents=docs, ids=ids)