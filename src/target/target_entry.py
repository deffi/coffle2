# from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.repository import RepositoryEntry
    from src.target import Target


@dataclass(frozen=True)
class TargetEntry:
    """An entry in a target. Contains a reference to the corresponding entry in
    the repository.

    Possible inconsistencies:
      * built and skipped

    """

    target: Target
    repository_entry: RepositoryEntry

    @property
    def relative_path(self) -> Path:
        return self.repository_entry.relative_target_path

    @property
    def target_file(self) -> Path:
        return self.target.root / self.relative_path

    @property
    def build_file(self) -> Path:
        return self.target.build_dir / self.relative_path

    @property
    def install_file(self) -> Path:
        return self.target.install_dir / self.relative_path

    @property
    def backup_file(self) -> Path:
        return self.target.backup_dir / self.relative_path

    @property
    def link_target(self) -> Path:
        return self.install_file.absolute().relative_to(self.target_file.parent.absolute())

