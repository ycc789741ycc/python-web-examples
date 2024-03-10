from typing import List

from app.domains.book_store.repository.base import BaseBookStoreRepository
from app.domains.book_store.models.book_store import BookStore


class InMemoryBookStoreRepository(BaseBookStoreRepository):
    def __init__(self):
        self.book_stores: List[BookStore] = []

    def get_all(self) -> List[BookStore]:
        return self.book_stores

    def get_by_id(self, book_store_id: str) -> BookStore:
        for book_store in self.book_stores:
            if book_store.id == book_store_id:
                return book_store
        return None

    def create(self, book_store: BookStore) -> BookStore:
        self.book_stores.append(book_store)
        return book_store

    def update_by_id(self, book_store_id: str, book_store: BookStore) -> None:
        for i, store in enumerate(self.book_stores):
            if store.id == book_store_id:
                self.book_stores[i] = book_store
                break

    def delete_by_id(self, book_store_id: str) -> None:
        to_remove_idx = None
        for i, store in enumerate(self.book_stores):
            if store.id == book_store_id:
                to_remove_idx = i
                break
        if to_remove_idx:
            self.book_stores.pop(to_remove_idx)
