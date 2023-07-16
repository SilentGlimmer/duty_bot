from pydantic import BaseModel


class UserSchema(BaseModel):
    class Config:
        from_attributes = True

    id: int
    first_name: str
    last_name: str
