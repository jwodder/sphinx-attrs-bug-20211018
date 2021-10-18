"""
Documenting attrs classes with Sphinx

Visit <https://github.com/jwodder/sphinx-attrs> or
<https://sphinx-attrs.rtfd.io> for more information.
"""

__version__ = "0.1.0.dev1"
__author__ = "John Thorvald Wodder II"
__author_email__ = "sphinx-attrs@varonathe.org"
__license__ = "MIT"
__url__ = "https://github.com/jwodder/sphinx-attrs"

from typing import List
import attr


@attr.define
class Foo:
    bar: int
    baz: str
    quux: List[str]
