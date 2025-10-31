from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("sample.pdf")
documents = loader.load()

print(documents)
print(documents[0])
print(documents[1].metadata)
print(type(documents[0]))
print(len(documents))