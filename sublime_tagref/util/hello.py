import sys


def hello() -> str:
    version = sys.version_info
    return f"Hello, Python {version.major}.{version.minor}.{version.micro}!"
