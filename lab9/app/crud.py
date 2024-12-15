from sqlalchemy.orm import Session
from .models import User, Post

# Создать пользователя
def create_user(db: Session, username: str, email: str, password: str):
    user = User(username=username, email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Создать пост
def create_post(db: Session, title: str, content: str, user_id: int):
    post = Post(title=title, content=content, user_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

# Получить всех пользователей
def get_users(db: Session):
    return db.query(User).all()

# Получить все посты
def get_posts(db: Session):
    return db.query(Post).all()

# Получить посты конкретного пользователя
def get_posts_by_user(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()

# Обновить email пользователя
def update_user_email(db: Session, user_id: int, new_email: str):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.email = new_email
        db.commit()
        db.refresh(user)
    return user

# Обновить содержимое поста
def update_post_content(db: Session, post_id: int, new_content: str):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        post.content = new_content
        db.commit()
        db.refresh(post)
    return post

# Удалить пользователя и его посты
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()

# Удалить пост
def delete_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
