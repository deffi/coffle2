from pathlib import Path


class Target:
    def __init__(self, root: Path):
        self._root = root

    @property
    def coffle_dir(self):
        return self._root / ".coffle"

    @property
    def build_dir(self):
        return self.coffle_dir / "build"

    @property
    def install_dir(self):
        return self.coffle_dir / "install"

    @property
    def backup_dir(self):
        return self.coffle_dir / "backup"
