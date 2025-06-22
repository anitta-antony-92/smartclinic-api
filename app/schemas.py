from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token:str
    token_type:str
    

class DoctorBase(BaseModel):
    name: str
    specialization: str
    email: EmailStr

class DoctorCreate(DoctorBase):
    pass

class DoctorOut(DoctorBase):
    id: int

    class Config:
        orm_mode = True
