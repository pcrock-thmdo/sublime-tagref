from pathlib import Path
from typing import List, Iterable, Optional

from sublime import CompletionFormat, CompletionItem, KIND_NAVIGATION, View, Window
import sublime_plugin

from ..util.tagref_process import TagRefProcess
from ..util.logging import get_logger


_logger = get_logger(__name__)


_process: Optional[TagRefProcess] = None


def _start_and_cache_new_process(folders: Iterable[str]) -> TagRefProcess:
    global _process
    paths = [Path(f) for f in folders]
    _process = TagRefProcess([p for p in paths if p.exists()])
    return _process


def _get_current_process(folders: Iterable[str]) -> TagRefProcess:
    if _process is not None:
        return _process
    return _start_and_cache_new_process(folders)


# https://www.sublimetext.com/docs/completions.html#plugins
class TagRefGlobalEventListener(sublime_plugin.EventListener):

    def on_query_completions(
        self,
        view: View,
        prefix: str,
        locations: list,
    ) -> List[CompletionItem]:
        tags = self._get_process(view).get_tags()
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

    def on_post_save(self, view: View) -> None:
        _logger.debug("refreshing cache after file save")
        self._refresh_cache(view)

    def on_revert(self, view: View) -> None:
        _logger.debug("refreshing cache after file revert")
        self._refresh_cache(view)

    def on_load_project(self, window: Window) -> None:
        _logger.debug("refreshing cache after project load")
        _start_and_cache_new_process(window.folders())

    def on_post_save_project(self, window: Window) -> None:
        _logger.debug("refreshing cache after project save")
        _start_and_cache_new_process(window.folders())

    def _get_process(self, view: View) -> TagRefProcess:
        return _get_current_process(view.window().folders())

    def _refresh_cache(self, view: View) -> TagRefProcess:
        return _start_and_cache_new_process(view.window().folders())
