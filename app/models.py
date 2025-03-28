from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

#Tabela de Utilizador
class User(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    name: str
    email: str
    password: str
    moods: List["Mood"] = Relationship(back_populates = "owner")

#Tabela do Humor
class Mood(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    date: Optional[datetime] = Field(default_factory=datetime.utcnow)
    mood: int
    commentary: str
    user_id: Optional[int] = Field(default = None, foreign_key = "user.id")
    owner: Optional["User"] = Relationship(back_populates = "moods")
    journals: List["Journal"] = Relationship(back_populates = "mood")

    

#Tabela do Diário
class Journal(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    date: Optional[datetime] = Field(default_factory=datetime.utcnow)
    title: str
    content: str
    mood_id: Optional[int] = Field(default = None, foreign_key = "mood.id")
    mood: Optional["Mood"] = Relationship(back_populates ="journals")