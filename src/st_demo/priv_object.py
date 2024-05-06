# langchain json output parse
# json object
from langchain_core.pydantic_v1 import BaseModel, Field

# Define your desired data structure.
# class Question(BaseModel):
#     question: str = Field(description="question to ask")
#     difficulty: str = Field(description="difficulty level of the question (easy, medium, hard)")

class Event(BaseModel):
    event_name: str = Field(description="event name")