from app.repositories import user_repository
class UserNotFoundError(Exception):
    pass

async def get_all_users():
    users = await user_repository.get_all()
    return users

async def get_spec_user(user_id:int):
    user = await user_repository.get_user(user_id)
    if user is None:
        raise UserNotFoundError("User Not found")
    return user