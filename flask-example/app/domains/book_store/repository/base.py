from abc import ABC, abstractmethod
from typing import List

from app.domains.book_store.models.book_store import BookStore


class BaseBookStoreRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[BookStore]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, book_store_id: str) -> BookStore:
        raise NotImplementedError

    @abstractmethod
    def create(self, book_store: BookStore) -> BookStore:
        raise NotImplementedError

    @abstractmethod
    def update_by_id(self, book_store_id: str, book_store: BookStore) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, book_store_id: str) -> None:
        raise NotImplementedError
