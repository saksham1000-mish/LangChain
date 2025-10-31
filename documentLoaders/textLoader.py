from langchain_community.document_loaders import TextLoader

loader = TextLoader("textfile.txt", encoding="utf8")

documents = loader.load()

print(documents)
print(documents[0])
print(type(documents[0]))
