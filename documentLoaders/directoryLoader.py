from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = 'books',
    glob = '*.pdf',
    loader_cls = PyPDFLoader
)

documents = loader.load()

print(documents)
print(documents[0])
print(documents[1].metadata)
print(type(documents[0]))
print(len(documents))