from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

prompt1 = PromptTemplate(
    template="Write a tweet about the following topic:\n\n{topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Write a linkedin post about the following topic:\n\n{topic}",
    input_variables=["topic"]
)
parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})

ans = parallel_chain.invoke({"topic": "AI"})
print(ans)
