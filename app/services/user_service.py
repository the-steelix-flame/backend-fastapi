from app.repositories import user_repository
from app.core.security import hash_password, verify_password, create_access_token

class UserAlreadyExistsError(Exception):
    pass
class UserNotFoundError(Exception):
    pass
class InvalidCredentialsError(Exception):
    pass



async def get_all_users(db):
    users = user_repository.get_all(db)
    return users

async def get_spec_user(db, user_id:int):
    user = user_repository.get_user(db, user_id)
    if user is None:
        raise UserNotFoundError("User Not found")
    return user

async def register_user(db, data):
    hashed_password = hash_password(data.password)
    try:
        return user_repository.create_user(
            db,
            data,
            password_hash = hashed_password
        )

    except user_repository.DuplicateEmailError:
        raise UserAlreadyExistsError()


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

async def authenticate_user(db, data):
    user = user_repository.get_user_by_email(
        db,
        data.email
    )

    if user is None:
        raise InvalidCredentialsError()

    if not verify_password(
        data.password,
        user.password_hash
    ):
        raise InvalidCredentialsError()
    
    token = create_access_token({"sub": str(user.id)})


    return {
        "access_token": token,
        "token_type": "bearer"
    }