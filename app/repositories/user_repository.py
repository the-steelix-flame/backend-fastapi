from sqlalchemy import select
from app.models.user import User

def get_all(db):
    stmt = select(User)
    return db.scalars(stmt).all()

def get_user(user_id: int, db):
    stmt = select(User).where(User.id == user_id)
    return db.scalars(stmt).first()

# print(get_user(3))