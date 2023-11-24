import sys

import sublime
import sublime_plugin


def hello() -> str:
    version = sys.version_info
    return f"Hello, Python {version.major}.{version.minor}.{version.micro}!"


class ExampleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, hello())
