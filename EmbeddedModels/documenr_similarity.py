from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embed = OpenAIEmbeddings(model ='text-embedding-3-small', dimensions=300)

documents = [
    "LangChain is a framework for developing applications powered by language models.",
    "It enables developers to build applications that can understand and generate human-like text.",
    "LangChain provides tools for prompt management, memory, and integration with various data sources.",
    "The sky is blue and the sun is shining.",
    "Artificial intelligence is transforming the world."
]

query = "What is LangChain?"
doc_embeddings = embed.embed_documents(documents)
query_embedding = embed.embed_query(query)

similarities = cosine_similarity([query_embedding], doc_embeddings)
most_similar_doc_index = np.argmax(similarities)

print("Most similar document:")
print(documents[most_similar_doc_index])