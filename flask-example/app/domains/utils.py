from uuid import uuid4


def id_generator() -> str:
    return str(uuid4())
