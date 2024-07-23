from fastapi import APIRouter, Form
from ..controllers.user_controller import User, UserController
import random

router = APIRouter()

@router.post('/user')
def create_user(name: str = Form(...), age: int = Form(...), address: str = Form(...)):
    user = User(name=name, age=age, address=address, id=random(4, 50))
    return UserController._create_user(user)

@router.get('/user/{id}')
def get_user(id: int):
    return UserController._get_user(id)
