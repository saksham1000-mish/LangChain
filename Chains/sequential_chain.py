# topic --> LLM --> report --> LLM --> summary
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template = "Generatte a detailed report about {topic}.", 
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template = "Summarize the following report in a concise manner:\n\n{report}", 
    input_variables=["report"]
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "space exploration"})

print(result)
chain.get_graph().print_ascii()