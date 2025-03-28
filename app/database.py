from sqlmodel import SQLModel, create_engine, Session
from app import models

# Conexão com o banco de dados SQLite
DATABASE_URL = "sqlite:///./meal_tracker.db"
engine = create_engine(DATABASE_URL, echo=True)

# Função para criar as tabelas no banco de dados
def init_session():
    SQLModel.metadata.create_all(bind=engine)

# Função para obter a sessão do banco de dados
def get_session():
    session = Session(engine)
    try:
        return session
    finally:
        session.close()
