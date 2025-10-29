from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm= HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

schema=[
    ResponseSchema(name='fact1', description='A fascinating fact1 about the topic.'),
    ResponseSchema(name='fact2', description='A fascinating fact2 about the topic.'),
    ResponseSchema(name='fact3', description='A fascinating fact3 about the topic.'),
]


parser = StructuredOutputParser.from_response_schema(schema)

template = PromptTemplate(
    template="Provide 3 fascinating facts about the topic: {topic} \n {format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

prompt = template.format(topic="Space Exploration")
result = model.invoke(prompt=prompt)

print(parser.parse(result.content))