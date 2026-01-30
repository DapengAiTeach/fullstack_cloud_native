from pydantic import BaseModel

class UserRegister(BaseModel):
    """用户注册模式"""
    username: str
    password: str

class UserLogin(UserRegister):
    """用户登录模式"""
    pass