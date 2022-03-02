import unittest
from pathlib import PurePosixPath as PPath, PureWindowsPath as WPath, Path

from file_name import unescape


class FileNameTest(unittest.TestCase):
    def test_unescape_str_simple(self):
        # Empty string or blanks only (why would you do this)
        self.assertEqual("", unescape(""))
        self.assertEqual("  ", unescape("  "))
        self.assertEqual(" _ ", unescape(" _ "))

        # Plain file name, might contain an underscore
        self.assertEqual("foo", unescape("foo"))
        self.assertEqual("foo_bar", unescape("foo_bar"))
        self.assertEqual("foobar_", unescape("foobar_"))

        # Dotfiles are also not modified, even with an underscore after the dot
        self.assertEqual(".bar", unescape(".bar"))
        self.assertEqual("._barbar", unescape("._barbar"))

    def test_unescape_str_escaped(self):
        # Empty string, just because it's invalid doesn't mean we can't unescape
        # it
        self.assertEqual("", unescape("_"))

        # Blank file name (variations on the theme)
        self.assertEqual(" ", unescape("_ "))

        # Escaped plain file
        self.assertEqual("baz", unescape("_baz"))

        # Escaped dotfile
        self.assertEqual(".qux", unescape("_.qux"))

        # Escaped file with an underscore
        self.assertEqual("_quux", unescape("__quux"))

    def test_unescape_path(self):
        # Clarify expectations: different path types don't compare equal
        self.assertNotEqual(WPath("foo"), PPath("foo"))

        # Paths unescape to the same type
        self.assertEqual(Path(".foo", ".bar"), unescape(Path("_.foo", "_.bar")))
        self.assertEqual(WPath(".foo", ".bar"), unescape(WPath("_.foo", "_.bar")))
        self.assertEqual(PPath(".foo", ".bar"), unescape(PPath("_.foo", "_.bar")))


if __name__ == '__main__':
    unittest.main()
