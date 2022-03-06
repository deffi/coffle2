from pathlib import Path
import unittest
from tempfile import TemporaryDirectory

from src.repository import Repository, RepositoryEntry


class RepositoryTest(unittest.TestCase):
    def test_entries(self):
        with TemporaryDirectory() as root:
            root = Path(root)

            (root / "foo").touch()
            (root / "bar").touch()
            (root / "subdir").mkdir()
            (root / "subdir" / "waldo").touch()
            (root / "subdir" / "fred").touch()

            repo = Repository(root)

            self.assertSetEqual({
                RepositoryEntry(repo, Path("foo")),
                RepositoryEntry(repo, Path("bar")),
                RepositoryEntry(repo, Path("subdir") / "waldo"),
                RepositoryEntry(repo, Path("subdir") / "fred"),
            }, set(repo.entries()))


if __name__ == '__main__':
    unittest.main()
