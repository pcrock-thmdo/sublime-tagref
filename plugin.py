from .sublime_tagref.util.module import dynamic_import
from .sublime_tagref.util import logging


logging.init(__package__)


TagRefGlobalEventListener = dynamic_import(
    ".event_listeners.global"
).TagRefGlobalEventListener


__all__ = [
    "TagRefGlobalEventListener",
]


def plugin_loaded() -> None:
    logger = logging.get_logger(__name__)
    logger.debug("sublime-tagref is loaded!")
