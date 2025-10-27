from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=0.5, max_tokens=5)

result = model.invoke("What is the capital of USA?")

print(result.content)