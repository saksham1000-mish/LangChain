from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="./Documents/sample.csv")

docs = loader.load()

print(docs[0].page_content)
print(len(docs))