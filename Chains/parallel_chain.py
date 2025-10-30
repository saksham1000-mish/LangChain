"""
           | --> model1 --> Notes --
document --                         |--> model3 --> output
           | --> model2 --> Quiz ---

"""
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
model2 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt1 = PromptTemplate(
    template="Generate shorts and simple notes about the following document:\n\n{document}",
    input_variables=["document"]
)

prompt2 = PromptTemplate(
    template="Create a quiz based on the following document:\n\n{document}",
    input_variables=["document"]
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document:\n\n{notes} and {quiz}",
    input_variables=["notes", "quiz"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes": prompt1 | model1 | parser,
    "quiz": prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
Artificial intelligence (AI) has rapidly evolved over the past decade, transforming various industries and aspects of daily life. From healthcare to finance, AI technologies are being leveraged to improve efficiency, accuracy, and decision-making processes. Machine learning, a subset of AI, enables systems to learn from data and make predictions or decisions without being explicitly programmed. As AI continues to advance, ethical considerations and regulatory frameworks are becoming increasingly important to ensure responsible development and deployment of these technologies.
"""

ans = chain.invoke({
    "document": text
})

print(ans)
chain.get_graph().print_ascii()