from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#Usado no POST
class UserCreate(BaseModel):
    name: str
    password: str
    email: str
    
    class Config:
        #Conversão SQL para Pydantic
        orm_mode = True 

#Usado no GET
class User(BaseModel):
    id: Optional[int]
    name: str

    class Config:
        #Conversão SQL para Pydantic
        orm_mode = True 

class MoodCreate(BaseModel):
    mood: int
    commentary: str
    user_id: Optional[int]

    class Config:
        #Conversão SQL para Pydantic
        orm_mode = True 

class Mood(BaseModel):
    id: Optional[int]
    date: datetime
    mood: int
    user_id: Optional[int]

    class Config:
        #Conversão SQL para Pydantic
        orm_mode = True 

class JournalCreate(BaseModel):
    title: str
    content: str
    mood_id: Optional[int]

    class Config:
        #Conversão SQL para Pydantic
        orm_mode = True 

class Journal(BaseModel):
    id: Optional[int]
    date:datetime
    title: str
    content: str    
    mood_id: Optional[int]

    class Config:
        #Conversão SQL para Pydantic
        orm_mode = True 