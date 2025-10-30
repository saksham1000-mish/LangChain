from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

prompt = PromptTemplate(
    template="Write a joke about the following topic:\n\n{topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Explain the joke:\n\n{joke}",
    input_variables=["joke"]
)
parser = StrOutputParser()

chain = RunnableSequence(
    prompt,
    model,
    parser,
    prompt2,
    model,
    parser
)

print(chain.invoke({"topic": "LangChain"}))
