from typing import Any

from business_logic import Command
from persistence import DatabaseManager
from persistence.database_manager import database_manager

db: DatabaseManager = database_manager()


class ListUserCommand(Command):
    def execute(self, data: dict = None) -> tuple[bool, Any]:
        return True, db.select("user").fetchall()
