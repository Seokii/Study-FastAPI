import datetime

from pydantic import BaseModel

class Question(BaseModel):
    id: int
    subject: str
    content: str | None = None
    create_date: datetime.datetime