from typing import Any

from business_logic import Command
from persistence import DatabaseManager, MovieWatchlistDatabase
from persistence.database_manager import database_manager

db: DatabaseManager = database_manager()


class ListMovieCommand(Command):
    def __init__(self, criteria: object = None, order_by: str = "id") -> None:
        self.criteria = criteria
        self.order_by = order_by

    def execute(self, data: dict = None) -> tuple[bool, Any]:
        return True, db.select(
            "movies", order_by=self.order_by, criteria=self.criteria
        ).fetchall()


if __name__ == "__main__":
    movie_watchlist = MovieWatchlistDatabase()
    upcomming_movies = ListMovieCommand(criteria={"release_date": "current_date"})
    print(upcomming_movies.execute())
