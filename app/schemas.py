from pydantic import BaseModel, EmailStr

# not being used atm
class Ambassadors(BaseModel):
    name: str
    email: EmailStr

    class Config():
        orm_mode = True
