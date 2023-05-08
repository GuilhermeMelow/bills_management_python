from typing import Generic, TypeVar


T = TypeVar("T")
G = TypeVar("G")


class Mapper(Generic[T, G]):
    def map(data: T) -> G:
        pass

    def map_invert(c: G) -> T:
        pass
