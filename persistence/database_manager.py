from persistence import DatabaseManager

database_file = "movie_watchlist.db"


def database_manager() -> DatabaseManager:
    return DatabaseManager(database_file)
