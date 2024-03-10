from dataclasses import dataclass


@dataclass
class Book:
    id: str
    name: str
    author: 'Author'
    price: float


@dataclass
class Author:
    id: str
    name: str
    age: int
