# create vectore datab at first time
# from app.ingest_service import *
from app.config import COLLECTION_NAME , VECTOR_DB_PATH
from langchain_chroma import Chroma
from app.llm_client import embedding_model

def get_vector_store():
    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embedding_model,
        persist_directory=VECTOR_DB_PATH
    )
    return vector_store