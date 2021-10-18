from typing import List
import attr

@attr.define
class Foo:
    bar: int
    baz: str
    quux: List[str]
