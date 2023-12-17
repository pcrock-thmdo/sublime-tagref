from pathlib import Path
import unittest

from sublime_tagref.util import logging
from sublime_tagref.util.tagref_process import TagRefProcess

TEST_TAG = "[tag:test-tagref-process]"
TEST_REF = "[ref:test-tagref-process]"
THIS_DIR = Path(__file__).parent

class TagRefProcessTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.init(__package__)

    def test_get_tags__always__returns_tag_in_this_file(self) -> None:
        tags = TagRefProcess([THIS_DIR]).get_tags()
        self.assertIn(TEST_TAG, tags)

    def test_get_valid_refs__always__returns_ref_for_this_file(self) -> None:
        refs = TagRefProcess([THIS_DIR]).get_valid_refs()
        self.assertIn(TEST_REF, refs)
