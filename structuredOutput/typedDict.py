from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI(model_name="gpt-3.5-turbo-0613", temperature=0)

review = " The product quality is excellent, but the delivery was delayed by two days."

class ReviewSummary(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(ReviewSummary)

result = structured_model.invoke(
    "Summarize the following product review and provide the overall sentiment (positive, negative, or neutral):"
    f"\n\nReview: {review}"
    )

print(result)