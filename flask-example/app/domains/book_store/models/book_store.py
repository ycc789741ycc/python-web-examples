from dataclasses import dataclass, field
from typing import List

from app.domains.book_store.models.book import Book


@dataclass
class BookStore:
    id: str
    name: str
    location: str
    books: List[Book] = field(default_factory=list)

    def is_book_existed(self, book: Book) -> bool:
        return book.id in [book.id for book in self.books]
