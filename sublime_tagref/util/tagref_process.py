from dataclasses import dataclass
from functools import lru_cache
import shutil
import subprocess
from typing import List

from .logging import get_logger


@lru_cache(maxsize=1)  # we would use `@cache`, but that was introduced in python 3.9 :'(
def find_tagref() -> str:
    executable_path = shutil.which("tagref")
    if executable_path is None:
        raise Exception("tagref executable not found.")
    return executable_path


REF_PREFIX = "ref"


@dataclass
class Tag:
    """
    the full tag string, ex. `[tag:tag-data-class]`
    """
    full_tag_str: str

    """
    the tag name, ex. `tag-data-class`
    """
    tag_name: str

    """
    the ref string you would use to reference the tag, ex. `[ref:tag-data-class]`
    """
    full_ref_str: str

    """
    the file path where the tag appears
    relative to the root directory where tagref was run
    """
    file_path: str

    """
    the line number in the file where the tag appears
    """
    line_number: int

    def __init__(self, tagref_output: str):
        parts = tagref_output.partition(" @ ")
        self.full_tag_str = parts[0]
        self.tag_name = parts[0].strip("[]").partition(":")[2]
        self.full_ref_str = f"[{REF_PREFIX}:{self.tag_name}]"

        location_parts = parts[2].rpartition(":")
        self.file_path = location_parts[0]
        self.line_number = int(location_parts[2])


def log_info(message: str):
    get_logger(__name__).info(message)


def log_warning(message: str):
    get_logger(__name__).warning(message)


class TagRefProcess():
    def __init__(self, folders: list):

        command = [find_tagref(), "list-tags"]
        log_info(f"running {command} for folders {folders}...")
        self._processes = [
            subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=f.__str__(),
            )
            for f in folders
        ]
        self._stdout: List[str] = None

    def _wait_for_results(self):
        if self._stdout is not None:
            return

        self._stdout = []
        stderr = []
        for p in self._processes:
            stdout_bytes, stderr_bytes = p.communicate(timeout=15)
            self._stdout.extend(stdout_bytes.decode("UTF8").splitlines())

            stderr.extend(stderr_bytes.decode("UTF8").splitlines())
            if p.returncode != 0:
                raise Exception(f"tagref exited with code {p.returncode}: {stderr}")

        if len(stderr) > 0:
            joined_stderr = "\n    ".join(stderr)
            log_warning(f"stderr: {joined_stderr}")

        self._processes = None

    def get_tags(self) -> List[Tag]:
        self._wait_for_results()
        return [
            Tag(line) for line in self._stdout
        ]
