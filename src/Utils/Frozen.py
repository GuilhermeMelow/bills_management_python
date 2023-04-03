from dataclasses import MISSING
from typing import Generic, TypeVar

# This isn't my implementation, source: https://stackoverflow.com/questions/61237131/how-to-make-attribute-in-dataclass-read-only

_T = TypeVar('_T')


class Frozen(Generic[_T]):
    __slots__ = (
        '_default',
        '_private_name',
    )

    def __init__(self, default: _T = MISSING):
        self._default = default

    def __set_name__(self, owner, name):
        self._private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self._private_name, self._default)

    def __set__(self, obj, value):
        if hasattr(obj, self._private_name):
            msg = f'Attribute `{self._private_name[1:]}` is immutable'
            raise TypeError(msg) from None

        setattr(obj, self._private_name, value)
