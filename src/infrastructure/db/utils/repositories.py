from abc import ABC, abstractmethod
from typing import Generic, List, NoReturn, TypeVar

# Define a generic type for your entities.
T = TypeVar('T')


class IRepository(ABC, Generic[T]):
    """
    Base repository interface.
    """
    model = None

    @abstractmethod
    def get_all(self) -> List[T]: pass

    @abstractmethod
    def filter_by(self, **kwargs) -> List[T]: pass

    @abstractmethod
    def get_one(self, **kwargs) -> T | None: pass

    @abstractmethod
    def delete(self, id: int | str) -> NoReturn: pass

    @abstractmethod
    def create(self, **kwargs) -> T: pass

    @abstractmethod
    def update(self, id: int | str, data: dict) -> T: pass
