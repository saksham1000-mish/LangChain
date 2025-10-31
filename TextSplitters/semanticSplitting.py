from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text = """LangChain is a framework for developing applications powered by language models. It can be used for chatbots, Generative Question-Answering (GQA), summarization, and much more.
Cricket is a bat-and-ball game played between two teams of eleven players on a field at the center of which is a 22-yard (20.12 m) pitch with a wicket at each end, each comprising two bails balanced on three stumps.Farmers of India have been facing numerous challenges in recent years, including unpredictable weather patterns, pest infestations, and fluctuating market prices for their crops. Many farmers have turned to sustainable farming practices to mitigate these issues, such as crop rotation, organic fertilizers, and integrated pest management.
"""

text_splitter = SemanticChunker(
    GoogleGenerativeAIEmbeddings(),
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)

docs = text_splitter.create_documents([text])
for i, doc in enumerate(docs):
    print(f"Document {i+1}:\n{doc.page_content}\n")