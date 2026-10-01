users = [
    {"id": 1, "name": "akash"},
    {"id": 2, "name": "rahul"},
    {"id": 3, "name": "ashita"}
]

async def get_all():
    return users

async def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
           return user
    return None

# print(get_user(3))