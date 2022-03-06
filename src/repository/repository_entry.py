from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.repository import Repository


@dataclass(frozen=True)
class RepositoryEntry:
    repository: Repository
    relative_path: Path
