from database import DatabaseManager
from .persistence import PersistenceLayer


class MovieWatchlistDatabase(PersistenceLayer):
    def __init__(self):
        self.user_table = "users"
        self.movie_table = "movies"
        self.user_watch_movie = "user_movie_watchlist"

        self.db = DatabaseManager("movie_watchlist.db")

        self.db.create_table(
            self.user_table,
            {"id": "INTEGER PRIMARY KEY AUTOINCREMENT", "name": "TEXT NOT NULL"},
        )

        self.db.create_table(
            self.movie_table,
            {
                "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
                "title": "TEXT NOT NULL",
                "release_date": "DATE",
            },
        )

        self.db.create_table(
            self.user_watch_movie,
            {
                "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
                "user_id": "INTEGER NOT NULL",
                "movie_id": "INTEGER NOT NULL",
                "is_watched": "tinyint default 0",
                "foreign key (user_id) references users(id)": "",
                "foreign key (movie_id) references movies(id)": "",
            },
        )

    def create(self, table_name: str, data: dict) -> None:
        self.db.add(table_name, data)

    def list(self, table_name: str, order_by: str = None) -> list:
        return self.db.select(table_name, order_by=order_by).fetchall()
