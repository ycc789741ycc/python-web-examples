from dataclasses import dataclass
from typing import List

from app.domains.book_store.models.book import Book


@dataclass
class BookStore:
    id: str
    name: str
    books: List[Book]
    location: str

    def is_book_existed(self, book: Book) -> bool:
        return book.id in [book.id for book in self.books]
