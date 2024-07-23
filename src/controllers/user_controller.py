from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: Optional[int] = None
    address: Optional[str] = None


class UserController:
    @staticmethod
    def _create_user(user: User):
        return {'message': "User Created!", 'user': user.dict()}
    
    @staticmethod
    def _get_user(id: int):
        return { 'user': { 'name': 'Test', 'id': id } }
    
