from app.config import MODEL_NAME , load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
# from sentence_transformers import SentenceTransformer
from langchain_huggingface import HuggingFaceEmbeddings

# general model
llm = ChatGroq(
    model_name=MODEL_NAME,
)
# Embedding 
embedding_model = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2',
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)

# translation model from english to arabic .
