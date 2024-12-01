from business_logic import Command, UserMovieWatchlist
from persistence import DatabaseManager, MovieWatchlistDatabase
from persistence.database_manager import database_manager

db: DatabaseManager = database_manager()


class AddUserMovieWatch(Command):
    def execute(self, data: dict = None) -> tuple[bool, None]:
        db.add("user_movie_watchlist", data)
        return True, None


if __name__ == "__main__":
    user_movie_watchlist = MovieWatchlistDatabase()
    data = UserMovieWatchlist(user_id=1, movie_id=1, is_watched=0)
    add_data = AddUserMovieWatch()
    add_data.execute(data.__dict__)
