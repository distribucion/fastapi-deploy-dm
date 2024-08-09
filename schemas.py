from pydantic import BaseModel


class ToDoRequest(BaseModel):
    name: str
    completed: bool


class ToDoResponse(BaseModel):
    name: str
    completed: bool
    id: int

    class Config:
        from_attributes = True
