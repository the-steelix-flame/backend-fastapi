from app.repositories import user_repository
class UserNotFoundError(Exception):
    pass

async def get_all_users(db):
    users = await user_repository.get_all(db)
    return users

async def get_spec_user(user_id:int, db):
    user = await user_repository.get_user(user_id, db)
    if user is None:
        raise UserNotFoundError("User Not found")
    return user