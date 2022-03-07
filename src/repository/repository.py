from pathlib import Path
from typing import Iterator

from src.repository import RepositoryEntry, IgnoreList


class Repository:
    def __init__(self, root: Path):
        self._root = root

    def _entries_in(self, directory: Path) -> Iterator[RepositoryEntry]:
        ignore_list = IgnoreList.load(directory / ".coffle_ignore")

        for item in directory.iterdir():
            if not (item.name.startswith(".") or ignore_list.matches(item.name)):
                if item.is_file():
                    yield RepositoryEntry(self, item.relative_to(self._root))
                elif item.is_dir():
                    yield from self._entries_in(item)
                else:
                    raise RuntimeError(f"Invalid repository entry: {item}")

    def entries(self) -> Iterator[RepositoryEntry]:
        yield from self._entries_in(self._root)
