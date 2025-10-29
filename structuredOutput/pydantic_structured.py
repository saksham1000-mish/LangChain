from pydantic import BaseModel, EmailStr, Field
from typing import Optional, TypedDict, Annotated
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

class Person(BaseModel):
    name: str
    age: int
    email: Optional[EmailStr] = None
    cgpa: float= Field(ge=0, le=10, description="CGPA must be between 0 and 10")

person = Person(name="Alice", age=30, email="alice@example.com", cgpa=9.5)

print(person)



model = ChatOpenAI(model_name="gpt-3.5-turbo-0613", temperature=0)

review = " The product quality is excellent, but the delivery was delayed by two days."

class ReviewSummary(BaseModel):
    key_themes: list[str] = Field(..., description="The key themes mentioned in the review.")
    summary: str = Field(..., description="The summary of the review.")
    sentiment: str = Field(..., description="The overall sentiment of the review.")
    pros: list[str] = Field(..., description="The positive aspects mentioned in the review.")
    cons: list[str] = Field(..., description="The negative aspects mentioned in the review.")

structured_model = model.with_structured_output(ReviewSummary)

result = structured_model.invoke(
    "Summarize the following product review and provide the overall sentiment (positive, negative, or neutral):"
    f"\n\nReview: {review}"
    )

print(result)


