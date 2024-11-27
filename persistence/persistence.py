from abc import ABC, abstractmethod


class PersistenceLayer(ABC):
    @abstractmethod
    def create(self, table_name: str, data: dict):
        raise NotImplementedError("Persistence layers must implement create method.")

    @abstractmethod
    def list(self, table_name: str, order_by: str = None):
        raise NotImplementedError("Persistence layers must implement list method.")

    @abstractmethod
    def edit(self, target_id: int, new_data: dict):
        raise NotImplementedError("Persistence layers must implement edit method.")

    @abstractmethod
    def delete(self, target_id: int):
        raise NotImplementedError("Persistence layers must implement delete method.")
