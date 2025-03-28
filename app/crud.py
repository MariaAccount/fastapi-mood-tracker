from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

# Instanciando o contexto de criptografia
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# ------------------ User ------------------------------
def get_users(session: Session):
    return session.query(models.User).all()

def get_user(session:Session, user_id: int):
    return session.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(session:Session, name: str):
    return session.query(models.User).filter(models.User.name == name).first()

def create_user(session:Session, user:schemas.UserCreate):
    password = pwd_context.hash(user.password)
    user = models.User(name = user.name, password = user.password, email = user.email)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def update_user(session: Session, user_id: int, user_update: schemas.UserCreate):
    user = session.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        return None
    user.name = user_update.name
    user.email = user_update.email
    user.password = user_update.password
    session.commit()
    session.refresh(user)
    return user

def delete_user(session: Session, user_id: int):
    user = session.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        return None
    session.delete(user)
    session.commit()
    return user

# ----------------- Mood -----------------------------
def create_mood(user_id: int, session: Session, mood: schemas.MoodCreate):
    session_mood = models.Mood(
        mood = mood.mood,
        commentary = mood.commentary,
        user_id = mood.user_id
    )
    session.add(session_mood)
    session.commit()
    session.refresh(session_mood)
    return session_mood

def get_all_moods_by_user(session: Session, user_id: int):
    return session.query(models.Mood).filter(models.Mood.user_id == user_id).all()

def get_mood(session: Session, user_id: int, id:int):
    return session.query(models.Mood).filter(models.Mood.user_id == user_id, models.Mood.id == id).first()

def update_mood(session: Session, user_id: int, id: int, mood_update: schemas.MoodCreate):
    mood = session.query(models.Mood).filter(models.Mood.id == id).first()
    if mood is None:
        return None
    mood.mood= mood_update.mood
    mood.commentary = mood_update.commentary
    session.commit()
    session.refresh(mood)
    return mood

def delete_mood(session: Session, user_id: int, id: int):
    mood = session.query(models.Mood).filter(models.Mood.id == id, models.Mood.user_id == user_id).first()
    if mood is None:
        return None
    session.delete(mood)
    session.commit()
    return mood

# ----------------------- Journal -----------------------------

def create_journal(mood_id: int, session: Session, journal: schemas.JournalCreate):
    session_journal = models.Journal(
        title = journal.title,
        content = journal.content,
        mood_id = journal.mood_id
    )
    session.add(session_journal)
    session.commit()
    session.refresh(session_journal)
    return session_journal

def get_all_journals_by_mood(session: Session, mood_id: int):
    return session.query(models.Journal).filter(models.Journal.mood_id == mood_id).all()

def get_journal(session: Session, mood_id: int, id:int):
    return session.query(models.Journal).filter(models.Journal.mood_id == mood_id, models.Journal.id == id).first()


def update_journal(session: Session, mood_id: int, id: int, journal_update: schemas.JournalCreate):
    journal = session.query(models.Journal).filter(models.Journal.id == id).first()
    if journal is None:
        return None
    journal.title= journal_update.title
    journal.content = journal_update.content
    session.commit()
    session.refresh(journal)
    return journal

def delete_journal(session: Session, mood_id: int, id: int):
    journal = session.query(models.Journal).filter(models.Journal.id == id, models.Journal.mood_id == mood_id).first()
    if journal is None:
        return None
    session.delete(journal)
    session.commit()
    return journal
