"""Keep same-named modules in different week folders from shadowing each other.

Several exercises are solved again in later weeks (``fuel.py``, ``plates.py``,
``bank.py``), so a plain ``import fuel`` would resolve to whichever copy was
imported first. Before a test file is imported, its own folder is put at the
front of ``sys.path`` and any cached module coming from a different folder is
dropped so the import picks up the sibling file.
"""

import sys
from pathlib import Path


def _isolate(directory):
    for path in directory.glob("*.py"):
        module = sys.modules.get(path.stem)
        if module is not None and getattr(module, "__file__", None) != str(path):
            del sys.modules[path.stem]

    folder = str(directory)
    if sys.path and sys.path[0] == folder:
        return
    if folder in sys.path:
        sys.path.remove(folder)
    sys.path.insert(0, folder)


def pytest_collectstart(collector):
    path = getattr(collector, "path", None)
    if path is not None and path.suffix == ".py":
        _isolate(path.parent)
