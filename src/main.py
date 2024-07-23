from fastapi import FastAPI
from .routes.user_route import router as user_router
import uvicorn

app = FastAPI()

app.include_router(user_router, prefix="/api")

# @app.get('/')
# async def root():
#     return { "message": "hello world" }

# @app.post('/')
# async def sendMessage(message):
#     print(message)
#     return { "message": message }

# @app.get('/{number}')
# async def showNumber(number: int):
#     return { 'number': number }

# class RoleEnum (str, Enum):
#     admin = "admin"
#     manager = "manager"

# @app.get('/user/{role}')
# async def showRole(role: RoleEnum) -> dict:
#     if(role == RoleEnum.manager):
#         return { "message": f'Your role is {role.value} thats kinda high'}
#     elif(role == RoleEnum.admin):
#         return { "message": f'Your role is {role.value} thats very high'}


if __name__ == "__main__":
    uvicorn.run(app, port=3000, reload=True)