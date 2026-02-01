from typing import Optional, Literal
from sqlalchemy.orm import Session
from sqlalchemy import select, asc, desc
from models import Movie

def create_movie(db: Session, movie: Movie) -> Movie:
    """创建新电影记录"""
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie

def get_movie(db: Session, movie_id: int) -> Optional[Movie]:
    """根据ID获取电影记录"""
    stmt = select(Movie).where(Movie.id == movie_id)
    result = db.execute(stmt).scalar_one_or_none()
    return result

def update_movie(db:Session, movie: Movie) -> Movie:
    """更新电影记录"""
    db.merge(movie)
    db.commit()
    db.refresh(movie)
    return movie

def delete_movie(db: Session, movie_id: int) -> None:
    """删除电影记录"""
    stmt = select(Movie).where(Movie.id == movie_id)
    movie = db.execute(stmt).scalar_one_or_none()
    if movie:
        db.delete(movie)
        db.commit()

def list_movies(
    db: Session, 
    page: int = 1,
    page_size: int = 10,
    sort_by: Literal["id", "release_year", "rating", "created_at"] = "created_at",
    sort_order: Literal["asc", "desc"] = "desc",
    keyword: Optional[str] = None,
) -> list[Movie]:
    """列出电影记录，支持分页和排序"""
    # 计算偏移量
    skip = (page - 1) * page_size
    # 计算排序方式
    order_func = asc if sort_order == "asc" else desc
    # 构建查询语句
    stmt = select(Movie).order_by(
        order_func(getattr(Movie, sort_by))
    ).offset(skip).limit(page_size)
    # 关键词过滤
    if keyword:
        stmt = stmt.where(
            Movie.title.contains(keyword) |
            Movie.director.contains(keyword) 
        )
    # 执行查询
    result = db.execute(stmt).scalars().all()
    # 返回结果
    return result