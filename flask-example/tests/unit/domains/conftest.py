import pytest

from app.domains.book_store.repository.in_memory import InMemoryBookStoreRepository


@pytest.fixture
def in_memory_book_store_repository():
    repository = InMemoryBookStoreRepository()
    return repository
