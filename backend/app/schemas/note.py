from pydantic import BaseModel

class NoteCreate(BaseModel):
    title : str
    content : str | None = None

class NoteUpdate(BaseModel):
    title : str
    content :  str  | None = None

class NoteResponse(BaseModel):
    id : int
    title : str
    content : str | None = None
    user_id : int

    model_config = {
        "from_attributes" : True
    }