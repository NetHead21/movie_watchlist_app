from typing import Any

from business_logic import Command
from persistence import DatabaseManager, MovieWatchlistDatabase
from persistence.database_manager import database_manager

db: DatabaseManager = database_manager()


class ListUserMovieWatchedCommand(Command):
    def __init__(self, criteria: object = None) -> None:
        self.criteria = criteria

    def execute(self, data: dict = None) -> tuple[bool, Any]:
        return True, db.select_with_join(
            data=data,
        ).fetchall()


