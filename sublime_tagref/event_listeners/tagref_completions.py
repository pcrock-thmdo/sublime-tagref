from pathlib import Path

import sublime_plugin

from ..util.tagref_process import TagRefProcess


# https://www.sublimetext.com/docs/completions.html#plugins
class TagRefCompletions(sublime_plugin.ViewEventListener):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        folders = [Path(f) for f in self.view.window().folders()]
        self._process = TagRefProcess([f for f in folders if f.exists()])

    def on_query_completions(
        self,
        prefix: str,
        locations: list,
    ) -> list:
        return self._process.get_valid_refs()
