from app.vector_store import get_vector_store
from app.config import K

def search_in_lectures(question):
    vector_store = get_vector_store()
    retriever = vector_store.as_retriever(search_kwargs={"k": K})
    results = retriever.invoke(question)
    return results