from langchain_classic.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("sample.pdf")
documents = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=2,
    separator=" ",
)
chunks = splitter.split_documents(documents)

print(chunks)