from sqlalchemy import select
from app.models.user import User

def get_all(db):
    stmt = select(User)
    return db.scalars(stmt).all()

def get_user(db, user_id: int):
    stmt = select(User).where(User.id == user_id)
    return db.scalars(stmt).first()

def create_user(db, user):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
