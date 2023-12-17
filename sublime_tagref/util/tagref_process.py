from dataclasses import dataclass
import shutil
import subprocess
from typing import List

from .logging import get_logger


@dataclass
class Tag:
    """
    the full tag string, ex. `[tag:foobar]`
    """
    full_tag_str: str

    """
    the tag name, ex. for `[tag:foobar]` it would be `foobar`
    """
    tag_name: str

    """
    the ref string you would use to reference the tag, ex. `[ref:foobar]`
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
        self.full_ref_str = f"[ref:{self.tag_name}]"

        location_parts = parts[2].rpartition(":")
        self.file_path = location_parts[0]
        self.line_number = int(location_parts[2])


class TagRefProcess():
    def __init__(self, folders: list):
        self._logger = get_logger(__name__)

        executable: str = shutil.which("tagref")
        if executable is None:
            raise Exception("tagref not found.")

        command = [executable, "list-tags"]
        self._logger.debug(f"running {command} for folders {folders}...")
        self._processes = [
            subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=f.__str__(),
            )
            for f in folders
        ]
        self._stdout: list = None
        self._stderr: list = None

    def _wait_for_results(self):
        if self._stdout is None:
            self._stdout = []
            self._stderr = []
            for p in self._processes:
                stdout_bytes, stderr_bytes = p.communicate(timeout=15)
                self._stdout.extend(stdout_bytes.decode("UTF8").splitlines())

                stderr = stderr_bytes.decode("UTF8").splitlines()
                self._stderr.extend(stderr)
                if p.returncode != 0:
                    raise Exception(f"tagref exited with code {p.returncode}: {stderr}")

            if len(self._stdout) > 0:
                joined_stdout = "\n    ".join(self._stdout)
                self._logger.debug(f"stdout:\n{joined_stdout}")
            if len(self._stderr) > 0:
                joined_stderr = "\n    ".join(self._stderr)
                self._logger.debug(f"stderr:\n{joined_stderr}")

        self._processes = None

    def get_tags(self) -> List[Tag]:
        self._wait_for_results()
        return [
            Tag(line) for line in self._stdout
        ]
