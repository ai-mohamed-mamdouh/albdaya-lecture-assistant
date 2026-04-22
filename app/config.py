from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

#LLM
TOP_P=0.7
TOP_K = 50
TEMPERATURE = 1
MODEL_NAME='qwen/qwen3-32b'

# load documents
FILE_PATH = str(BASE_DIR / "data" / "raw" / "ML project (1).pdf")

# Splite to chunks
CHUNK_SIZE=200
CHUNK_OVERLAP=10
K=4

# Embedding
EMBEDDING_MODEL_NAME="sentence-transformers/all-MiniLM-L6-v2"


VECTOR_DB_PATH = str(BASE_DIR / "data" / "vectordb")
COLLECTION_NAME = "albdaya_lectures"