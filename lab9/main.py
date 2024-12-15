from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import Base, engine, SessionLocal
from app.crud import *
from app.models import User, Post

# Создание таблиц
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Получение сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Маршрут для создания пользователя
@app.post("/users/")
def create_user_route(username: str, email: str, password: str, db: Session = Depends(get_db)):
    return create_user(db, username, email, password)

# Маршрут для создания поста
@app.post("/posts/")
def create_post_route(title: str, content: str, user_id: int, db: Session = Depends(get_db)):
    return create_post(db, title, content, user_id)

# Получить всех пользователей
@app.get("/users/")
def get_users_route(db: Session = Depends(get_db)):
    return get_users(db)

# Получить все посты
@app.get("/posts/")
def get_posts_route(db: Session = Depends(get_db)):
    return get_posts(db)

# Получить посты конкретного пользователя
@app.get("/posts/{user_id}")
def get_posts_by_user_route(user_id: int, db: Session = Depends(get_db)):
    return get_posts_by_user(db, user_id)

# Обновить email пользователя
@app.put("/users/{user_id}")
def update_user_email_route(user_id: int, new_email: str, db: Session = Depends(get_db)):
    user = update_user_email(db, user_id, new_email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Удалить пользователя
@app.delete("/users/{user_id}")
def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    delete_user(db, user_id)
    return {"message": "User deleted"}
