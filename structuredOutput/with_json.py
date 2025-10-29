from pydantic import BaseModel, Field
from typing import Optional, TypedDict, Annotated
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model_name="gpt-3.5-turbo-0613", temperature=0)

review = " The product quality is excellent, but the delivery was delayed by two days."

json_schema ={
    "title": "ReviewSummary",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {"type": "string"},
            "description": "The key themes mentioned in the review."
        },
        "summary": {
            "type": "string",
            "description": "The summary of the review."
        },
        "sentiment": {
            "type": "string",
            "description": "The overall sentiment of the review."
        },
        "pros": {
            "type": "array",
            "items": {"type": "string"},
            "description": "The positive aspects mentioned in the review."
        },
        "cons": {
            "type": "array",
            "items": {"type": "string"},
            "description": "The negative aspects mentioned in the review."
        }
    },
    "required": ["key_themes", "summary", "sentiment", "pros", "cons"]
}

structured_model = model.with_structured_output(json_schema=json_schema )

result = structured_model.invoke(
    "Summarize the following product review and provide the overall sentiment (positive, negative, or neutral):"
    f"\n\nReview: {review}"
    )

print(result)


