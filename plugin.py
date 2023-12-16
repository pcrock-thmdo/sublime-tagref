from .sublime_tagref.event_listeners.tagref_completions import TagRefCompletions
from .sublime_tagref.util import logging


__all__ = [
    "TagRefCompletions",
]


def plugin_loaded() -> None:
    logging.init(__package__)
    logger = logging.get_logger(__name__)
    logger.debug("sublime-tagref is loaded!")
