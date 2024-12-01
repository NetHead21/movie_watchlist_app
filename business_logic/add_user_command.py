from business_logic import Command, User
from persistence import DatabaseManager
from persistence.database_manager import database_manager
from persistence.movie_watchlist_database import MovieWatchlistDatabase

db: DatabaseManager = database_manager()


class AddUserCommand(Command):
    def execute(self, data: dict = None) -> tuple[bool, None]:
        db.add("users", data)
        return True, None


if __name__ == "__main__":
    movie_watchlist = MovieWatchlistDatabase()
    user = User(name="Juniven")
    add_user = AddUserCommand()
    add_user.execute(user.__dict__)
