from app.repositories import order_repository
from app.repositories import user_repository

class UserNotFoundError(Exception):
    pass

async def create_order(db, data):
    user = user_repository.get_user(db, data.user_id)

    if user is None:
        raise UserNotFoundError()

    return order_repository.create_order(db, data)