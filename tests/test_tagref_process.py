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
        self.assertIn(TEST_TAG, [t.full_tag_str for t in tags])
        self.assertIn(TEST_REF, [t.full_ref_str for t in tags])
