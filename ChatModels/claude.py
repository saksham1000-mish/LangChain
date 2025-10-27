from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-3.5-sonnet-20241022', temperature=0.5, max_completion_tokens=5)

result = model.invoke("What is the capital of India?")
print(result.content)