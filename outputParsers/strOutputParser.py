from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm= HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

template1=PromptTemplate(
    template="Give me a motivational quote about {topic}.",
    input_variables=["topic"]
)
template2=PromptTemplate(
    template="Give me a 5 line summary on the following text. /n {text}.",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser
result = chain.invoke(topic="perseverance")

print(result)  