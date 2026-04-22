from langchain_core.output_parsers import StrOutputParser

from app.llm_client import llm
from app.prompts import rag_prompt
from app.rag_service import search_in_lectures

def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])

def out_put(user_input):
    docs = search_in_lectures(user_input)
    context = format_docs(docs)

    chain = rag_prompt | llm | StrOutputParser()

    return chain.invoke({
        "context": context,
        "question": user_input
    })


