users = [{1:"akash"},{2:"rahul"},{3:"ashita"}]

async def get_all():
    return users

async def get_user(user_id: int):
    for user in users:
        if user_id in user:
            return user
    return None

# print(get_user(3))