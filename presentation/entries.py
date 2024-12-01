from datetime import date
from business_logic import User, Movie, UserMovieWatchlist
from presentation import get_user_input, format_date


def get_new_user() -> User:
    try:
        name = get_user_input("Enter New User Name: ")
        return User(name=name)
    except ValueError:
        print("Some error in entry occur, please try again.")


def get_new_movie() -> Movie:
    try:
        title = get_user_input("Enter New Movie Title: ")
        release_date = get_user_input("Enter New Movie Release Date: ")
        return Movie(title=title, release_date=date(format_date(release_date)))
    except ValueError:
        print("Some error in entry occur, please try again.")


def get_user_movie_watchlist() -> UserMovieWatchlist:
    try:
        user_id = get_user_input("Enter User ID: ")
        movie_id = get_user_input("Enter Movie ID: ")
        return UserMovieWatchlist(user_id=user_id, movie_id=movie_id, is_watched=0)

    except ValueError:
        print("Some error in entry occur, please try again.")
