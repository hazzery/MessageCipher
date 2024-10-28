"""Test package for MessageCipher."""

import pathlib
import sys

PROJECT_PATH = pathlib.Path.cwd()
SOURCE_PATH = pathlib.Path(PROJECT_PATH) / "src"
sys.path.append(str(SOURCE_PATH.absolute))
