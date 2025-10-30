from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough, RunnableLambda, RunnableBranch

load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a detailed report on about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text in a concise manner:\n\n{text}',
    input_variables=['text']
)


report_gen = RunnableSequence(prompt, model, parser)
branch_chain = RunnableBranch(
    (lambda x: len(x) > 300, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen, branch_chain)
result = final_chain.invoke({'topic': 'Artificial Intelligence'})
print(result)