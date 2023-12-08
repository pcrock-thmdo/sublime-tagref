import sublime


# https://www.sublimetext.com/docs/api_reference.html#sublime.CompletionList
class TagRefCompletionList(sublime.CompletionList):
    def __init__(self):
        super().__init__(
            completions=None,
            flags=sublime.AutoCompleteFlags.INHIBIT_WORD_COMPLETIONS
        )
        # TODO: call tagref, and then self.set_completions()
