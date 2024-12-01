from typing import Any

from business_logic import Command
from persistence import DatabaseManager
from persistence.database_manager import database_manager

db: DatabaseManager = database_manager()


class ListMovieCommand(Command):
    def __init__(self, criteria: dict = None, order_by: str = "id") -> None:
        self.order_by = order_by
        self.criteria = criteria

    def execute(self, data: dict = None) -> tuple[bool, Any]:
        return True, db.select("movies", order_by=self.order_by).fetchone()
