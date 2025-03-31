from pydantic import BaseModel, ConfigDict
from typing import List , Optional

class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)



class User(BaseModel):
    id: int
    name: str
    email: str
    password: Optional[str] = None

    # model_config = ConfigDict(from_attributes=True)