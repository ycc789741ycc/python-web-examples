from typing import List

from app.domains.book_store.constants import MAX_SELLING_BOOK_PRICE, MIN_SELLING_BOOK_PRICE
from app.domains.book_store.exceptions import BookExisted, BookPriceNotValid
from app.domains.book_store.repository.base import BaseBookStoreRepository
from app.domains.book_store.models.book import Book


class BookStoreService:
    def __init__(self, book_store_repository: BaseBookStoreRepository):
        self.book_store_repository = book_store_repository

    def get_all(self):
        return self.book_store_repository.get_all()

    def get_by_id(self, book_store_id: str):
        return self.book_store_repository.get_by_id(book_store_id)

    def create(self, book_store):
        return self.book_store_repository.create(book_store)

    def update(self, book_store_id: str, book_store):
        return self.book_store_repository.update_by_id(book_store_id, book_store)

    def delete(self, book_store_id: str):
        return self.book_store_repository.delete_by_id(book_store_id)
    
    def add_selling_books(self, book_store_id, books: List[Book]) -> None:
        book_store = self.book_store_repository.get_by_id(book_store_id)
        for book in books:
            self._validate_book_price(book)
            self._validate_book_is_existed(book_store_id, book)
            book_store.books.append(book)
        self.book_store_repository.update_by_id(book_store_id, book_store)

    def _validate_book_price(self, book: Book) -> None:
        if book.price < MIN_SELLING_BOOK_PRICE or book.price > MAX_SELLING_BOOK_PRICE:
            raise BookPriceNotValid(f'Book price must be between {MIN_SELLING_BOOK_PRICE} and {MAX_SELLING_BOOK_PRICE}')

    def _validate_book_is_existed(self, book_store_id, book: Book) -> None:
        book_store = self.book_store_repository.get_by_id(book_store_id)
        if book_store.is_book_existed(book):
            raise BookExisted(f'Book {book.id} is existed in book store {book_store_id}')
    
    def add_free_books(self, book_store_id, books: List[Book]) -> None:
        book_store = self.book_store_repository.get_by_id(book_store_id)
        for book in books:
            self._validate_book_is_existed(book_store_id, book)
            self._validate_book_is_free(book)
            book_store.books.append(book)
        self.book_store_repository.update_by_id(book_store_id, book_store)
    
    def _validate_book_is_free(self, book: Book) -> None:
        if book.price != 0:
            raise BookPriceNotValid(f'Book price must be 0')
