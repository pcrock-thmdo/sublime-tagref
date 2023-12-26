from pathlib import Path
from typing import List, Iterable, Optional

from sublime import CompletionFormat, CompletionItem, KIND_NAVIGATION, View
import sublime_plugin

from ..util.tagref_process import TagRefProcess
from ..util.logging import get_logger


_logger = get_logger(__name__)


_process: Optional[TagRefProcess] = None


def get_process(folders: Iterable[str]) -> TagRefProcess:
    global _process
    if _process is not None:
        return _process
    paths = [Path(f) for f in folders]
    _process = TagRefProcess([p for p in paths if p.exists()])
    return _process


# https://www.sublimetext.com/docs/completions.html#plugins
class TagRefGlobalEventListener(sublime_plugin.EventListener):

    def on_query_completions(
        self,
        view: View,
        prefix: str,
        locations: list,
    ) -> List[CompletionItem]:
        folders = view.window().folders()
        tags = get_process(folders).get_tags()
        completion_items = [
            CompletionItem(
                t.full_ref_str,
                annotation="tagref",
                completion=t.full_ref_str,
                completion_format=CompletionFormat.TEXT,
                kind=KIND_NAVIGATION,
            ) for t in tags
        ]
        _logger.info(f"got {len(completion_items)} completion items")
        return completion_items
