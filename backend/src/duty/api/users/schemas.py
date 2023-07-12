from pydantic import BaseModel


class UserSchema(BaseModel):
    class Config:
        orm_mode = True

    id: int
    first_name: str
    last_name: str
