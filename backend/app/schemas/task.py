from pydantic import BaseModel
from datetime import date
from typing import Optional


class TaskCreate(BaseModel):
    title: str
    description: str
    status: str
    project_id: int
    assigned_to: Optional[int] = None
    due_date: date
