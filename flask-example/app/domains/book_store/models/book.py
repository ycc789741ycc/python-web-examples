from dataclasses import dataclass, field
from uuid import uuid4, UUID


@dataclass
class Book:
    name: str
    author: 'Author'
    price: float
    id: UUID = field(default_factory=uuid4)


@dataclass
class Author:
    name: str
    age: int
    id: UUID = field(default_factory=uuid4)
