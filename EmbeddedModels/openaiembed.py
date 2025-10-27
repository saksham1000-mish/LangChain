from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embed = OpenAIEmbeddings(model ='text-embedding-3-small', dimensions=32)

result = embed.embed_query("Hello world")
print(result)