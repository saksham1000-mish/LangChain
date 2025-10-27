from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embed = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2" )

result = embed.embed_query("Hello world")
print(str(result))