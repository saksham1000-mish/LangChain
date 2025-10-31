from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

prompt1 = PromptTemplate(
    template="Answer the following question: \n{question} based on the content of the webpage:\n\n{document}",
    input_variables=["question","document"]
)
parser = StrOutputParser()

url = "https://api.python.langchain.com/en/latest/runnables/langchain_core.runnables.base.RunnableParallel.html"

loader = WebBaseLoader(url)

documents = loader.load()

chain = prompt1 | model1 | parser

chain.invoke({
    "document": documents[0].page_content,
    "question": "What is RunnableParallel?"
})