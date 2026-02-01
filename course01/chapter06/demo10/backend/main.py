import crud

from typing import List, Optional, Literal
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Movie
from schemas import MovieCreate, MovieUpdate, MovieResponse

# 创建主程序
app = FastAPI(title="电影管理API", version="0.1.0")

# 创建数据库表
Base.metadata.create_all(bind=engine)

# 依赖项：获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/movies/", response_model=MovieResponse)
def create_movie(
    movie: MovieCreate, 
    db: Session = Depends(get_db)
) -> MovieResponse:
    """创建新电影记录"""
    db_movie = Movie(
        title=movie.title,
        director=movie.director,
        genre=movie.genre,
        rating=movie.rating,
        release_year=movie.release_year,
    )
    created_movie = crud.create_movie(db, db_movie)
    return created_movie

@app.get("/movies/{movie_id}", response_model=MovieResponse)
def read_movie(
    movie_id: int, 
    db: Session = Depends(get_db)
) -> MovieResponse:
    """根据ID获取电影记录"""
    db_movie = crud.get_movie(db, movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="电影未找到")
    return db_movie

@app.put("/movies/{movie_id}", response_model=MovieResponse)
def update_movie(
    movie_id: int,
    movie: MovieUpdate,
    db: Session = Depends(get_db)
) -> MovieResponse:
    """更新电影记录"""
    db_movie = crud.get_movie(db, movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="电影未找到")
    for var, value in vars(movie).items():
        if value is not None:
            setattr(db_movie, var, value)
    updated_movie = crud.update_movie(db, db_movie)
    return updated_movie

@app.delete("/movies/{movie_id}", response_model=None)
def delete_movie(
    movie_id: int,
    db: Session = Depends(get_db)
) -> None:
    """删除电影记录"""
    db_movie = crud.get_movie(db, movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="电影未找到")
    crud.delete_movie(db, movie_id)
    return None

@app.get("/movies/", response_model=List[MovieResponse])
def list_movies(
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(10, ge=1, le=100, description="每页记录数"),
    sort_by: Literal["id", "release_year", "rating", "created_at"] = Query(
        "created_at", description="排序字段"
    ),
    sort_order: Literal["asc", "desc"] = Query(
        "desc", description="排序方式"
    ),
    keyword: Optional[str] = Query(None, description="搜索关键词"),
    db: Session = Depends(get_db)
) -> List[MovieResponse]:
    """列出电影记录，支持分页和排序"""
    movies = crud.list_movies(
        db,
        page=page,
        page_size=page_size,
        sort_by=sort_by,
        sort_order=sort_order,
        keyword=keyword,
    )
    return movies