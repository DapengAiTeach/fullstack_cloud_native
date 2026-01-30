from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from config.database import engine, init_db
from apps.simplelogin.models import User
from apps.simplelogin.schemas import UserRegister, UserLogin
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有请求头
)

@app.on_event("startup")
def on_startup():
    """应用启动时初始化数据库"""
    init_db()
    print("数据库初始化完成")

@app.post("/register/")
def register_user(user: UserRegister):
    """用户注册接口"""
    with Session(engine) as session:
        # 根据用户名查询用户
        statement = select(User).where(User.username == user.username)
        # 判断用户名是否已存在
        existing_user = session.exec(statement).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="用户名已存在")
        # 添加新用户
        db_user = User(username=user.username, password=user.password)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
    return {"message": "用户注册成功", "user_id": db_user.id}

@app.post("/login/")
def login_user(user: UserLogin):
    """用户登录接口"""
    with Session(engine) as session:
        # 根据用户名查询用户
        statement = select(User).where(User.username == user.username)
        # 判断用户是否存在且密码是否正确
        existing_user = session.exec(statement).first()
        if not existing_user or existing_user.password != user.password:
            raise HTTPException(status_code=400, detail="用户名或密码错误")
    return {"message": "登录成功", "user_id": existing_user.id}