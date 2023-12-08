import sublime
import sublime_plugin

# from ..tagref_completion_list import TagRefCompletionList


# https://www.sublimetext.com/docs/completions.html#plugins
class TagRefCompletions(sublime_plugin.EventListener):
    def on_query_completions(
        self,
        view: sublime.View,
        prefix: str,
        locations: list[sublime.Point]
    ) -> sublime.CompletionList:
        print("completions queried!")
        return ["hi"]
        # if prefix.lower() == "[ref:":
        #     return TagRefCompletionList()
        # else:
        #     return []
