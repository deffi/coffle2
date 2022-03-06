from fnmatch import fnmatchcase
from pathlib import Path
from typing import List

# TODO support comments, but allows escaping #


class IgnoreList:
    def __init__(self, patterns: List[str]):
        self.patterns = patterns

    @classmethod
    def load(cls, file: Path):
        # Read patterns from file
        patterns = [pattern.strip() for pattern in file.read_text().splitlines()]

        # Remove empty strings
        patterns = [pattern for pattern in patterns if pattern]

        return cls(patterns)

    def matches(self, name: str):
        # We could make this more efficient by converting the patterns to a
        # regex:
        #     re.compile('|'.join(fnmatch.translate(p) for p in self.patterns))

        return any(fnmatchcase(name, pattern) for pattern in self.patterns)
