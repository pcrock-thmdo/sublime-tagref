import shutil
import subprocess

from .logging import get_logger


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

    def get_tags(self) -> list:
        self._wait_for_results()
        return [
            line.partition(" @ ")[0] for line in self._stdout
        ]

    def get_valid_refs(self) -> set:
        return {
            f"[ref{parts[1]}{parts[2]}]" for parts in
            (tag.strip("[]").partition(":") for tag in self.get_tags())
        }
