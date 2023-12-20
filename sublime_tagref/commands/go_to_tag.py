import sublime
import sublime_plugin

from ..util.logging import get_logger


logger = get_logger(__name__)


class GoToTagCommand(sublime_plugin.WindowCommand):
    def run(self):
        window = self.window()
        if view := window.active_view() is None:
            logger.warning("no active view")
            return

        # the Open URL plugin has figured this stuff out pretty well
        # we just need some simpler logic
        # Command Palette -> View Package File -> Open Url/open_url.py
        # find OpenUrlCommand
