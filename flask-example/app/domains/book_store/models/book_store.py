from dataclasses import dataclass, field
from uuid import uuid4, UUID
from typing import List

from app.domains.book_store.models.book import Book


@dataclass
class BookStore:
    name: str
    location: str
    books: List[Book] = field(default_factory=list)
    id: UUID = field(default_factory=uuid4)

    def is_book_existed(self, book: Book) -> bool:
        return book.id in [book.id for book in self.books]
