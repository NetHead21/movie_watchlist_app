from datetime import date
from pydantic import BaseModel


class Movie(BaseModel):
    title: str
    release_date: date


class User(BaseModel):
    name: str


class UserMovieWatchlist(BaseModel):
    user_id: int
    movie_id: int
    is_watched: int


if __name__ == "__main__":
    name = User(name="Juniven")
    print(name.__dict__)
