from datetime import date

from business_logic import Command, Movie
from persistence import DatabaseManager
from persistence.database_manager import database_manager
from persistence.movie_watchlist_database import MovieWatchlistDatabase

db: DatabaseManager = database_manager()


class AddMovieCommand(Command):
    def execute(self, data: dict = None) -> tuple[bool, None]:
        db.add("movies", data)
        return True, None


if __name__ == "__main__":
    movie_watchlist = MovieWatchlistDatabase()
    movie = Movie(title="The Avatar", release_date=date(2009, 12, 15))
    add_movie = AddMovieCommand()
    add_movie.execute(movie.__dict__)
