import sublime_plugin

from ..util.hello import hello

class InsertHelloCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, hello())
