from pathlib import Path

from sublime import CompletionFormat, CompletionItem, KIND_NAVIGATION, View
import sublime_plugin

from ..util.tagref_process import TagRefProcess
from ..util.logging import get_logger


logger = get_logger(__name__)


def get_process(view: View) -> TagRefProcess:
    folders = [Path(f) for f in view.window().folders()]
    return TagRefProcess([f for f in folders if f.exists()])


# https://www.sublimetext.com/docs/completions.html#plugins
class TagRefCompletions(sublime_plugin.EventListener):

    def on_query_completions(
        self,
        view: View,
        prefix: str,
        locations: list,
    ) -> list:
        refs = get_process(view).get_valid_refs()
        completion_items = [
            CompletionItem(
                r.strip("[]").partition(":")[2],
                annotation=r,
                completion=r,
                completion_format=CompletionFormat.TEXT,
                kind=KIND_NAVIGATION,
            ) for r in refs
        ]
        logger.debug(f"got completion items {completion_items}")
        return completion_items
