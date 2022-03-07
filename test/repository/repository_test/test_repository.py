from pathlib import Path
import unittest

from src.repository import Repository, RepositoryEntry


class RepositoryTest(unittest.TestCase):
    def test_entries(self):
        repo = Repository(Path(__file__).parent / "test_entries")

        self.assertSetEqual({
            RepositoryEntry(repo, Path("foo")),
            RepositoryEntry(repo, Path("bar")),
            RepositoryEntry(repo, Path("subdir") / "waldo"),
            RepositoryEntry(repo, Path("subdir") / "fred"),
        }, set(repo.entries()))


if __name__ == '__main__':
    unittest.main()
