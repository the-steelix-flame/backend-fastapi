from sqlalchemy import select
from app.models.user import User
from sqlalchemy.exc import IntegrityError

class DuplicateEmailError(Exception):
    pass

class UserNotFoundError(Exception):
    pass

def get_all(db):
    stmt = select(User)
    return db.scalars(stmt).all()

def get_user(db, user_id: int):
    stmt = select(User).where(User.id == user_id)
    return db.scalars(stmt).first()

def create_user(db, user):
    new_user = User(**user.model_dump())
    db.add(new_user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise DuplicateEmailError()
    db.refresh(new_user)
    return new_user



def update_user(db, user_id, data):
    user = get_user(db, user_id)

    if user is None:
        return None

    user.name = data.name
    user.email = data.email

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise DuplicateEmailError()

    db.refresh(user)
    return user

def delete_user(db, user_id):
    user = get_user(db, user_id)

    if user is None:
        raise UserNotFoundError()

    db.delete(user)
    db.commit()