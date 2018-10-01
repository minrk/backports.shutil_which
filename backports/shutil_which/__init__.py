"""Backport of shutil.which from Python 3.5

The function is included unmodified from Python stdlib 3.5.1,
and is (C) Python
"""

from .shutil_which import which


__all__ = ['which']

__version__ = '3.5.1'
