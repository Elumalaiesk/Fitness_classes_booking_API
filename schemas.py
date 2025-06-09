from datetime import datetime
from pydantic import BaseModel # type: ignore

class ClassResponse(BaseModel):
    id: int
    name: str
    datetime: datetime
    instructor: str
    available_slots: int

    class Config:
        orm_mode = True

class BookingResponse(BaseModel):
    class_id: int
    class_name: str
    class_time: datetime
    client_name: str
    client_email: str

class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: str
