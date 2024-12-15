from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import *

db: Session = SessionLocal()

# Добавление пользователей
user1 = create_user(db, "user1", "user1@example.com", "password1")
user2 = create_user(db, "user2", "user2@example.com", "password2")

# Добавление постов
post1 = create_post(db, "Post 1", "Content for Post 1", user1.id)
post2 = create_post(db, "Post 2", "Content for Post 2", user2.id)

# Извлечение пользователей и постов
print(get_users(db))
print(get_posts(db))
