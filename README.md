
## Setup and Installation

1.  **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create a `.env` file:**
    Create a `.env` file in the root directory and add your API keys. See the `.gitignore` file to ensure it's not committed.
    ```env
    OPENAI_API_KEY="your-openai-api-key"
    GOOGLE_API_KEY="your-google-api-key"
    ANTHROPIC_API_KEY="your-anthropic-api-key"
    HUGGINGFACEHUB_API_TOKEN="your-huggingface-api-token"
    ```

3.  **Install dependencies:**
    It is recommended to use a virtual environment.
    ```sh
    pip install -r requirements.txt
    ```

## Usage and Examples

Each folder contains scripts that can be run directly to see the component in action.

### Chains

-   [`Chains/simple_chain.py`](Chains/simple_chain.py): A basic chain that takes a topic and generates facts.
-   [`Chains/sequential_chain.py`](Chains/sequential_chain.py): A chain where the output of one model is the input to the next.
-   [`Chains/parallel_chain.py`](Chains/parallel_chain.py): Runs multiple chains in parallel and merges their outputs.
-   [`Chains/conditional_chain.py`](Chains/conditional_chain.py): A chain that routes logic based on the input, using `RunnableBranch`.

### Chat Models

-   [`ChatModels/openai.py`](ChatModels/openai.py): Demonstrates usage of OpenAI's GPT models.
-   [`ChatModels/gemini.py`](ChatModels/gemini.py): Shows how to use Google's Gemini models.
-   [`ChatModels/claude.py`](ChatModels/claude.py): Example of using Anthropic's Claude models.
-   [`ChatModels/huggingface.py`](ChatModels/huggingface.py): Interacting with models from the Hugging Face Hub.

### Document Loaders

-   [`documentLoaders/textLoader.py`](documentLoaders/textLoader.py): Loads a plain `.txt` file.
-   [`documentLoaders/pdfLoader.py`](documentLoaders/pdfLoader.py): Loads content from a `.pdf` file.
-   [`documentLoaders/csvLoader.py`](documentLoaders/csvLoader.py): Loads data from a `.csv` file.
-   [`documentLoaders/directoryLoader.py`](documentLoaders/directoryLoader.py): Loads all files of a specific type from a directory.
-   [`documentLoaders/webBaseLoader.py`](documentLoaders/webBaseLoader.py): Scrapes and loads content from a URL.

### Embedding Models

-   [`EmbeddedModels/openaiembed.py`](EmbeddedModels/openaiembed.py): Generates a vector embedding for a query using OpenAI.
-   [`EmbeddedModels/embedHF.py`](EmbeddedModels/embedHF.py): Uses a Hugging Face sentence-transformer model for embeddings.
-   [`EmbeddedModels/documenr_similarity.py`](EmbeddedModels/documenr_similarity.py): Calculates cosine similarity between a query and a list of documents.

### Output Parsers

-   [`outputParsers/strOutputParser.py`](outputParsers/strOutputParser.py): The default parser that returns the model's output as a string.
-   [`outputParsers/jsonOutputParser.py`](outputParsers/jsonOutputParser.py): Parses the model's output into a JSON object.
-   [`outputParsers/pydanticOutputParser.py`](outputParsers/pydanticOutputParser.py): Parses the output into a Pydantic model for data validation.
-   [`outputParsers/structuredOutputParsers.py`](outputParsers/structuredOutputParsers.py): Uses `ResponseSchema` to define a desired JSON structure.

### Retrievers

-   [`Retriever/langchain_retrievers.ipynb`](Retriever/langchain_retrievers.ipynb): A Jupyter notebook demonstrating the use of `WikipediaRetriever` and a vector store-backed retriever (`Chroma`).

### Runnables

-   [`runnables/runnableSequence.py`](runnables/runnableSequence.py): Demonstrates chaining runnables sequentially.
-   [`runnables/runnaleParallel.py`](runnables/runnaleParallel.py): Shows how to execute runnables in parallel on the same input.
-   [`runnables/runnablePassthrough.py`](runnables/runnablePassthrough.py): Illustrates how to pass inputs through a chain unmodified.
-   [`runnables/runnableLambda.py`](runnables/runnableLambda.py): Using custom functions as part of a chain.
-   [`runnables/runnableBranch.py`](runnables/runnableBranch.py): Implementing conditional logic in a chain.

### Structured Output

-   [`structuredOutput/pydantic_structured.py`](structuredOutput/pydantic_structured.py): Using a Pydantic class to define the output schema.
-   [`structuredOutput/typedDict.py`](structuredOutput/typedDict.py): Using Python's `TypedDict` for schema definition.
-   [`structuredOutput/with_json.py`](structuredOutput/with_json.py): Providing a raw JSON schema to structure the model's output.

### Text Splitters

-   [`TextSplitters/lengthBased.py`](TextSplitters/lengthBased.py): Splits text by character count using `CharacterTextSplitter`.
-   [`TextSplitters/textStructureBased.py`](TextSplitters/textStructureBased.py): Splits text recursively based on separators like newlines using `RecursiveCharacterTextSplitter`.
-   [`TextSplitters/pythonCodeSplitting.py`](TextSplitters/pythonCodeSplitting.py): Splits Python code while respecting its structure.
-   [`TextSplitters/semanticSplitting.py`](TextSplitters/semanticSplitting.py): Splits text into chunks based on semantic similarity using `SemanticChunker`.

## Notes

For a deeper understanding of the concepts used in this repository, refer to the following files:

-   [**notes.txt**](notes.txt): Comprehensive notes covering fundamental LangChain components.
-   [**RAGNotes.txt**](RAGNotes.txt): Detailed explanation of the Retrieval-Augmented Generation (RAG) pattern.