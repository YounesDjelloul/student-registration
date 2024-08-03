from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class StudentApplication(BaseModel):
    name: str
    email: str
    course: str
    application_date: datetime = Field(default_factory=datetime.utcnow)
    id: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com",
                "course": "Computer Science"
            }
        }
