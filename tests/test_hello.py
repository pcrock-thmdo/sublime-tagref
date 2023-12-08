import unittest

from sublime_tagref.util.hello import hello


class TestCase(unittest.TestCase):
    def test_hello__always__returns_python_version(self) -> None:
        self.assertEqual(hello(), "Hello, Python 3.8.12!")
