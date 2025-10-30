"""
                  +ve| --> model1 --> Thanks ---
feedback --model1--                           |--> model3 --> output
                  -ve| --> model2 --> Resolve ---

"""
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser1 = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="You are a customer support agent, classify the following feedback as positive or negative:\n\n{feedback} \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={'format_instructions': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template="Generate a thank you message for the following positive feedback:\n\n{feedback}",
    input_variables=["feedback"]
)
prompt3 = PromptTemplate(
    template="Generate a resolution message for the following negative feedback:\n\n{feedback}",
    input_variables=["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment=='positive' , prompt2 | model | parser1),
    (lambda x:x.sentiment=='negative', prompt3 | model | parser1),
    RunnableLambda(lambda x: "Sentiment must be either 'positive' or 'negative'")
)

chain = classifier_chain | branch_chain

text = "The product quality is outstanding and exceeded my expectations!"

print(chain.invoke({
    "feedback": text
}))
chain.get_graph().print_ascii()