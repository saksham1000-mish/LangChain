from langchain_classic.text_splitter import RecursiveCharacterTextSplitter

text = """LangChain is a framework for developing applications powered by language models. It can be used for chatbots, Generative Question-Answering (GQA), summarization, and much more.
LangChain provides a standard interface for all LLMs, as well as a toolkit of components to build applications. It also provides integrations with other data sources and tools, such as vector databases, APIs, and document loaders.
"""
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
)
chunks = splitter.split_text(text)
print(len(chunks))
print(chunks)