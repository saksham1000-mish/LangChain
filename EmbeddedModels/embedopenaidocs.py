from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embed = OpenAIEmbeddings(model ='text-embedding-3-small', dimensions=32)

docs = [
    "LangChain is a framework for developing applications powered by language models.",
    "It enables developers to build applications that can understand and generate human-like text.",
    "LangChain provides tools for prompt management, memory, and integration with various data sources."
]

result = embed.embed_documents(docs)
print(result)