from functools import singledispatch
from pathlib import PurePath
from typing import TypeVar

P = TypeVar("P", bound=PurePath)

@singledispatch
def unescape(name):
    raise TypeError(f"Invalid file name: {name}")


@unescape.register
def _(name: str) -> str:
    """Unescape a file name: remove a single underscore at the beginning"""
    if name == "":
        return ""
    elif name[0] == '_':
        return name[1:]
    else:
        return name


@unescape.register(PurePath)
def _(path: P) -> P:
    return type(path)(*(unescape(part) for part in path.parts))
