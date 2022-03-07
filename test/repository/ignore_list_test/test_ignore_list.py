from pathlib import Path
import unittest

from src.repository import IgnoreList


class IgnoreListTest(unittest.TestCase):
    def test_matches(self):
        ignore_list = IgnoreList([
            "foo.txt",
            "ba*.txt",
            "waldo",
            "*.tmp"
        ])

        self.assertTrue(ignore_list.matches("foo.txt"))
        self.assertTrue(ignore_list.matches("ba.txt"))
        self.assertTrue(ignore_list.matches("bar.txt"))
        self.assertTrue(ignore_list.matches("barbara.txt"))
        self.assertTrue(ignore_list.matches("waldo"))
        self.assertTrue(ignore_list.matches("ephemeral.tmp"))
        self.assertTrue(ignore_list.matches(".tmp"))

        self.assertFalse(ignore_list.matches("foofoo.txt"))
        self.assertFalse(ignore_list.matches("foobar.txt"))
        self.assertFalse(ignore_list.matches("waldont"))

    def test_load(self):
        ignore_list = IgnoreList.load(Path(__file__).parent / "test_load" / "ignore_list.txt")

        self.assertListEqual([
            "foo",
            "foo.txt",
            "ba*.txt",
            "waldo",
            "*.tmp",
        ], ignore_list.patterns)


if __name__ == '__main__':
    unittest.main()
