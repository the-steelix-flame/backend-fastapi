from app.repositories import user_repository
from app.core.security import hash_password

class UserAlreadyExistsError(Exception):
    pass
class UserNotFoundError(Exception):
    pass


async def get_all_users(db):
    users = user_repository.get_all(db)
    return users

async def get_spec_user(db, user_id:int):
    user = user_repository.get_user(db, user_id)
    if user is None:
        raise UserNotFoundError("User Not found")
    return user

async def create_user(db, data, password_hash):
    try:
        return user_repository.create_user(db, data, password_hash)

    except user_repository.DuplicateEmailError:
        raise UserAlreadyExistsError()


async def register_user(db, data):
    hashed_password = hash_password(data.password)

    return user_repository.create_user(
        db,
        data,
        password_hash = hashed_password
    )


async def update_user(db, user_id, data):
    try:
        user = user_repository.update_user(db, user_id, data)

        if user is None:
            raise UserNotFoundError()

        return user

    except user_repository.DuplicateEmailError:
        raise UserAlreadyExistsError()

async def delete_user(db, user_id):
    try:
        return user_repository.delete_user(db, user_id)
    except user_repository.UserNotFoundError:
        raise UserNotFoundError()