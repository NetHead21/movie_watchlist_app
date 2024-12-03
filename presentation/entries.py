from datetime import date
from typing import Any

from business_logic import User, Movie, UserMovieWatchlist
from presentation import get_user_input, format_date


def get_new_user() -> dict[str, Any]:
    try:
        name = get_user_input("Enter New User Name: ")
        return User(name=name).__dict__
    except ValueError:
        print("Some error in entry occur, please try again.")


def get_new_movie() -> dict[str, Any]:
    try:
        title = get_user_input("Enter New Movie Title: ")
        release_date = get_user_input("Enter New Movie Release Date: ")
        year, month, day = format_date(release_date)
        return Movie(title=title, release_date=date(year, month, day)).__dict__
    except ValueError:
        print("Some error in entry occur, please try again.")


def get_user_movie_watchlist() -> dict[str, Any]:
    try:
        user_id = get_user_input("Enter User ID: ")
        movie_id = get_user_input("Enter Movie ID: ")
        return UserMovieWatchlist(
            user_id=user_id, movie_id=movie_id, is_watched=1
        ).__dict__

    except ValueError:
        print("Some error in entry occur, please try again.")


def get_user_id() -> dict[str, Any]:
    try:
        user_id = get_user_input("Enter User ID: ")
        return UserMovieWatchlist(user_id=user_id, movie_id=1, is_watched=1).__dict__

    except ValueError:
        print("Some error in entry occur, please try again.")
