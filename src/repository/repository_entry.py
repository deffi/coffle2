from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

from src.repository import file_name

if TYPE_CHECKING:
    from src.repository import Repository


@dataclass(frozen=True)
class RepositoryEntry:
    repository: Repository
    relative_path: Path

    @property
    def relative_target_path(self) -> Path:
        return file_name.unescape(self.relative_path)

    @property
    def source_file(self) -> Path:
        return self.repository.root / self.relative_path
