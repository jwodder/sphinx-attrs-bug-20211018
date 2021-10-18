""" Documenting attrs classes with Sphinx """

__version__ = "0.1.0.dev1"
__author__ = "John Thorvald Wodder II"
__author_email__ = "sphinx-attrs@varonathe.org"
__license__ = "MIT"

from typing import List
import attr


@attr.define
class Foo:
    """This class was created with ``@attr.define``."""

    bar: int
    baz: str
    quux: List[str]


@attr.s
class Bar:
    """This class was created with ``@attr.s``."""

    bar: int
    baz: str
    quux: List[str]
