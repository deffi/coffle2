from pathlib import Path
from typing import Iterator

from src.repository import RepositoryEntry

class Repository:
    def __init__(self, root: Path):
        self._root = root

    def entries(self) -> Iterator[RepositoryEntry]:
        for directory in self._root.rglob(""):
            # TODO .coffleignore
            for file in directory.iterdir():
                if file.is_file():
                    yield RepositoryEntry(self, file.relative_to(self._root))