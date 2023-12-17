import unittest

from sublime_tagref.util import logging
from sublime_tagref.util.module import dynamic_import


class UtilModuleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.init(__package__)

    def test_dynamic_import__module_exists__returns_module(self) -> None:
        module = dynamic_import(".util.tagref_process")
        self.assertIsNotNone(module.TagRefProcess)

    def test_dynamic_import__module_does_not_exist__throws(self) -> None:
        with self.assertRaises(Exception):
            dynamic_import(".foo.bar.baz.dkjdkdkdk")
