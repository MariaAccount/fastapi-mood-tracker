# Mood Tracker API

A backend API built with **FastAPI**, **SQLModel** and **SQLite** that allows users to track their moods and link them to journal entries.

# Features

- **User Management**: Create, update, and delete users
- **Mood Tracking**: Users can log moods with a numeric value and a commentary
- **Journal Entries**: Link journal entries to specific moods
- **Password Hashing** using `passlib`
- **Relational Database Design** using SQLModel + SQLAlchemy relationships
- **SQLite** for local testing



# Installation and Usage

## 1. Clone the repository

```bash
git clone https://github.com/MariaAccount/fastapi-mood-tracker.git
cd fastapi-mood-tracker
```
## 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  
```
## 3.Install dependencies
```bash
pip install -r requirements.txt
```

## 4. Iniciate API with FastAPI + Uvicorn
```bash
uvicorn app.main:app --reload
```


# Data Models

## User
```python
- id: int
- name: str
- email: str
- password: str
- moods: List[Mood]
```
## Mood
```python
- id: int
- date: datetime (auto-filled)
- mood: int (e.g., scale from 1 to 5)
- commentary: str
- user_id: int (FK -> User)
- journals: List[Journal]
```
## Journal
```python
- id: int
- date: datetime (auto-filled)
- title: str
- content: str
- mood_id: int (FK -> Mood)
```

# Example API Endpoints

## Users

- `GET /users/` – List all users  
- `POST /users/` – Create a user  
- `GET /users/{user_id}` – Get a user  
- `PUT /users/{user_id}` – Update a user  
- `DELETE /users/{user_id}` – Delete a user  

## Moods

- `GET /users/{user_id}/moods/` – List moods by user  
- `POST /users/{user_id}/moods/` – Add a mood  
- `GET /users/{user_id}/moods/{id}/` – Get a specific mood  
- `PUT /users/{user_id}/moods/{id}/` – Update a mood  
- `DELETE /users/{user_id}/moods/{id}/` – Delete a mood  

## Journals

- `POST /users/{user_id}/moods/{mood_id}/journals/` – Create a journal entry  
- `GET /users/{user_id}/moods/{mood_id}/journals/` – List journals for a mood  
- `GET /users/{user_id}/moods/{mood_id}/journals/{id}` – Get a journal  
- `PUT /users/{user_id}/moods/{mood_id}/journals/{id}` – Update a journal  
- `DELETE /users/{user_id}/moods/{mood_id}/journals/{id}` – Delete a journal  

# Technologies Used

- **Python 3.12** 
- **FastAPI**
- **SQLModel**
- **Passlib (bcrypt)**
- **Uvicorn**
- **SQLite**
- **SQLAlchemy** 


# 📁 Folder Structure
```
project-root/
│
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI app entry point
│   ├── models.py          # SQLModel database models
│   ├── schemas.py         # Pydantic schemas
│   ├── crud.py            # CRUD operations
│   └── database.py        # DB connection and session
│
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
└── .gitignore             # Git ignored files
```

# Future Ideas

- Build a user-friendly frontend using **React.js**
- Improve mood representation with emojis or color scales