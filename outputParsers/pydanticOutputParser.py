from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm= HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str = Field(description="The person's full name")
    age: int = Field(description="The person's age in years")
    email: str = Field(description="The person's email address")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Provide details about a person including their name, age, and email address in the following format: {format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

prompt = template.format()
result = model.invoke(prompt=prompt)
print(parser.parse(result.content))

