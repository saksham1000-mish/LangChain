from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm= HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)
parser = JsonOutputParser()

template1 = PromptTemplate(
    template="Give me name, age and city of a fictional person \n {format_instructions}",
    input_variables=["format_instructions"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
prompt = template1.format()

result = model.invoke(prompt=prompt)

print(parser.parse(result.content))  