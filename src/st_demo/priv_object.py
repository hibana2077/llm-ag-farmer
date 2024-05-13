'''
Author: hibana2077 hibana2077@gmail.com
Date: 2024-05-06 11:54:17
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-05-08 13:59:27
FilePath: \llm-ag-farmer\src\st_demo\priv_object.py
Description: This file is for model output parsing
'''
# langchain json output parse
# json object
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum

class EventStatus(str, Enum):
    PLANNED = 'Planned'
    ONGOING = 'Ongoing'
    COMPLETED = 'Completed'
    CANCELED = 'Canceled'
    ERROR = 'Error'

class FunctionCall(str, Enum):
    PLANTING_SCHEDULE = 'planting_schedule'
    STATUS_CHECK = 'status_check'
    TROUBLESHOOTING = 'troubleshooting'
    HARVEST_ANALYSIS = 'harvest_analysis'
    EDUCATION_TRAINING = 'education_training'

class Event(BaseModel):
    event_name: str = Field(..., description="The name of the event")
    description: Optional[str] = Field(None, description="Detailed description of the event")
    start_date: datetime = Field(..., description="Start date of the event")
    end_date: datetime = Field(..., description="End date of the event")
    notes: Optional[str] = Field(None, description="Additional notes for the event")
    status: EventStatus = Field(default=EventStatus.PLANNED, description="Current status of the event")

class Schedule(BaseModel):
    schedule_name: str = Field(..., description="The name of the schedule")
    events: List[Event] = Field(..., description="List of events in the schedule")
    created_at: datetime = Field(default_factory=datetime.now, description="Creation date of the schedule")
    updated_at: Optional[datetime] = Field(None, description="Last updated date of the schedule")

class Task(BaseModel):
    task_name: str = Field(..., description="The name of the task")
    description: Optional[str] = Field(None, description="Detailed description of the task")
    due_date: datetime = Field(..., description="Due date of the task")
    notes: Optional[str] = Field(None, description="Additional notes for the task")
    status: EventStatus = Field(default=EventStatus.PLANNED, description="Current status of the task")

# Example of creating a schedule
my_schedule = Schedule(
    schedule_name="Spring Planting",
    events=[
        Event(
            event_name="Tomato Planting",
            description="Planting tomatoes in the greenhouse",
            start_date=datetime(2024, 3, 15),
            end_date=datetime(2024, 3, 15),
            status=EventStatus.PLANNED
        ),
        Event(
            event_name="Lettuce Harvest",
            description="Harvesting mature lettuce",
            start_date=datetime(2024, 6, 1),
            end_date=datetime(2024, 6, 2),
            status=EventStatus.PLANNED
        )
    ]
)
