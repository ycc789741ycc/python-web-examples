import pytest

from app.domains.book_store.models.book import Book, Author
from app.domains.book_store.models.book_store import BookStore
from app.domains.book_store.repository.base import BaseBookStoreRepository
from app.domains.book_store.repository.in_memory import InMemoryBookStoreRepository
from app.domains.book_store.service.service import BookStoreService
from app.domains.book_store.exceptions import BookPriceNotValid


def test_get_all(in_memory_book_store_repository: InMemoryBookStoreRepository):
    book_store_service = BookStoreService(in_memory_book_store_repository)

    book_store_1 = BookStore(name="Book Store 1", location="Location 1")
    book_store_2 = BookStore(name="Book Store 2", location="Location 2")
    book_store_service.create(book_store_1)
    book_store_service.create(book_store_2)

    # Call the get_all method
    book_stores = book_store_service.get_all()

    # Assert that the returned books match the added books
    assert len(book_stores) == 2
    assert book_store_1 in book_stores
    assert book_store_2 in book_stores


def test_get_by_id(in_memory_book_store_repository: InMemoryBookStoreRepository):
    book_store_service = BookStoreService(in_memory_book_store_repository)

    book_store_1 = BookStore(name="Book Store 1", location="Location 1")
    book_store_2 = BookStore(name="Book Store 2", location="Location 2")
    book_store_service.create(book_store_1)
    book_store_service.create(book_store_2)

    # Call the get_by_id method
    retrieved_book_store = book_store_service.get_by_id(book_store_1.id)

    # Assert that the retrieved book matches the added book
    assert retrieved_book_store == book_store_1


def test_add_selling_books(
    in_memory_book_store_repository: InMemoryBookStoreRepository,
):
    book_store_service = BookStoreService(in_memory_book_store_repository)

    book_store = BookStore(name="Book Store 1", location="Location 1")
    book_store_service.create(book_store)

    author_1 = Author(name="Author 1", age=30)
    book_1 = Book(name="Book 1", author=author_1, price=10)
    author_2 = Author(name="Author 2", age=40)
    book_2 = Book(name="Book 2", author=author_2, price=20)

    # Call the add_selling_books method
    book_store_service.add_selling_books(book_store.id, [book_1, book_2])

    # Assert that the books are added to the book store
    retrieved_book_store = book_store_service.get_by_id(book_store.id)
    assert book_1 in retrieved_book_store.books
    assert book_2 in retrieved_book_store.books


def test_add_selling_books_with_invalid_price(
    in_memory_book_store_repository: InMemoryBookStoreRepository,
):
    book_store_service = BookStoreService(in_memory_book_store_repository)

    book_store = BookStore(name="Book Store 1", location="Location 1")
    book_store_service.create(book_store)

    author_1 = Author(name="Author 1", age=30)
    book_1 = Book(name="Book 1", author=author_1, price=1000)

    # Call the add_selling_books method
    with pytest.raises(BookPriceNotValid):
        book_store_service.add_selling_books(book_store.id, [book_1])


def test_add_free_books(in_memory_book_store_repository: InMemoryBookStoreRepository):
    book_store_service = BookStoreService(in_memory_book_store_repository)

    book_store = BookStore(name="Book Store 1", location="Location 1")
    book_store_service.create(book_store)

    author_1 = Author(name="Author 1", age=30)
    book_1 = Book(name="Book 1", author=author_1, price=0)
    author_2 = Author(name="Author 2", age=40)
    book_2 = Book(name="Book 2", author=author_2, price=0)

    # Call the add_free_books method
    book_store_service.add_free_books(book_store.id, [book_1, book_2])

    # Assert that the books are added to the book store
    retrieved_book_store = book_store_service.get_by_id(book_store.id)
    assert book_1 in retrieved_book_store.books
    assert book_2 in retrieved_book_store.books


def test_add_free_books_with_invalid_price(
    in_memory_book_store_repository: InMemoryBookStoreRepository,
):
    book_store_service = BookStoreService(in_memory_book_store_repository)

    book_store = BookStore(name="Book Store 1", location="Location 1")
    book_store_service.create(book_store)

    author_1 = Author(name="Author 1", age=30)
    book_1 = Book(name="Book 1", author=author_1, price=10)

    # Call the add_free_books method
    with pytest.raises(BookPriceNotValid):
        book_store_service.add_free_books(book_store.id, [book_1])
