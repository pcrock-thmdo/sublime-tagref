from importlib import import_module
from typing import Any


BASE_MODULE_NAME = __package__.rpartition(".util")[0]
# when sublime is running, this will be `sublime-tagref.sublime_tagref`
# when non-sublime tests are running, this will be `sublime_tagref`


def dynamic_import(module: str) -> Any:
    return import_module(module, BASE_MODULE_NAME)
