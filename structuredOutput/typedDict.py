from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model = ChatOpenAI(model_name="gpt-3.5-turbo-0613", temperature=0)

review = " The product quality is excellent, but the delivery was delayed by two days."

class ReviewSummary(TypedDict):
    key_themes: Annotated[list[str], "The key themes mentioned in the review."]
    summary: Annotated[str, "The summary of the review."]
    sentiment: Annotated[str, "The overall sentiment of the review."]
    pros: Annotated[list[str], "The positive aspects mentioned in the review."]
    cons: Annotated[list[str], "The negative aspects mentioned in the review."] 

structured_model = model.with_structured_output(ReviewSummary)

result = structured_model.invoke(
    "Summarize the following product review and provide the overall sentiment (positive, negative, or neutral):"
    f"\n\nReview: {review}"
    )

print(result)