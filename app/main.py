from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import init_session, get_session
from typing import List

#Cria as tabelas
init_session()

app = FastAPI()
#---------------------------User---------------------------

#GET todos os utilizadores
@app.get("/users/", response_model = List[schemas.User])
def get_users(session: Session = Depends(get_session)):
    return crud.get_users(session)

#GET um utilizador específico
@app.get("/users/{user_id}", response_model = schemas.User)
def get_user(user_id: int, session: Session = Depends(get_session)):
    return crud.get_user(session, user_id)

#GET com nome utilizador
@app.get("/users/name/{name}", response_model = schemas.User)
def get_user_by_name(name: str, session: Session = Depends(get_session)):
    return crud.get_user_by_username(session, name)

#POST com utilizador
@app.post("/users/", response_model = schemas.User)
def create_user(user:schemas.UserCreate, session: Session = Depends(get_session)):
    return crud.create_user(session, user)

#PUT com utilizador
@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user_update: schemas.UserCreate, session: Session = Depends(get_session)):
    session_user = crud.update_user(session, user_id, user_update)
    if session_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return session_user

#DELETE com utilizador
@app.delete("/users/{user_id}", response_model = schemas.User)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    session_user = crud.delete_user(session, user_id)
    if session_user is None:
        raise HTTPException(status_code = 404, detail = "User not found")
    return session_user

# ----------------Mood ------------------------------------------

#POST com mood
@app.post("/users/{user_id}/moods/", response_model = schemas.Mood)
def create_mood(user_id: int, mood:schemas.MoodCreate, session: Session = Depends(get_session)):
    return crud.create_mood(user_id, session, mood)

#GET com mood
@app.get("/users/{user_id}/moods/", response_model = List[schemas.Mood])
def get_all_moods_by_user(user_id: int,session: Session = Depends(get_session)):
    return crud.get_all_moods_by_user(session, user_id)


#GET com mood
@app.get("/users/{user_id}/moods/{id}/", response_model = schemas.Mood)
def get_mood(user_id: int, id: int, session: Session = Depends(get_session)):
    return crud.get_mood(session, user_id,id)

#PUT com mood
@app.put("/users/{user_id}/moods/{id}/",response_model = schemas.Mood)
def update_mood(user_id: int, id: int,mood_update: schemas.MoodCreate, session: Session = Depends(get_session)):
    return crud.update_mood(session, user_id, id, mood_update)


#DELETE com mood
@app.delete("/users/{user_id}/moods/{id}", response_model = schemas.Mood)
def delete_mood(user_id: int, id: int, session: Session = Depends(get_session)):
    session_mood = crud.delete_mood(session, user_id, id)
    if session_mood is None:
        raise HTTPException(status_code = 404, detail = "Mood not found")
    return session_mood

# ----------------- Journal -----------------------------

#POST com journal
@app.post("/users/{user_id}/moods/{mood_id}/journals/", response_model = schemas.Journal)
def create_journal(user_id: int, mood_id: int, journal:schemas.JournalCreate, session: Session = Depends(get_session)):
    return crud.create_journal(mood_id, session, journal)

#GET com journal
@app.get("/users/{user_id}/moods/{mood_id}/journals/", response_model = List[schemas.Journal])
def get_all_journals_by_mood(user_id: int, mood_id: int,session: Session = Depends(get_session)):
    return crud.get_all_journals_by_mood(session, mood_id)


#GET com journal
@app.get("/users/{user_id}/moods/{mood_id}/journals/{id}", response_model = schemas.Journal)
def get_journal(user_id: int, mood_id: int, id: int, session: Session = Depends(get_session)):
    return crud.get_journal(session, mood_id,id)

#PUT com journal
@app.put("/users/{user_id}/moods/{mood_id}/journals/{id}",response_model = schemas.Journal)
def update_journal(user_id: int, mood_id: int, id: int,journal_update: schemas.JournalCreate, session: Session = Depends(get_session)):
    return crud.update_journal(session, mood_id, id, journal_update)

#DELETE com journal
@app.delete("/users/{user_id}/moods/{mood_id}/journals/{id}", response_model = schemas.Journal)
def delete_journal(mood_id: int, id: int, session: Session = Depends(get_session)):
    session_journal = crud.delete_journal(session, mood_id, id)
    if session_journal is None:
        raise HTTPException(status_code = 404, detail = "journal not found")
    return session_journal