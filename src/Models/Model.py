
from dataclasses import dataclass
from uuid import UUID, uuid4

from src.Utils.Frozen import Frozen


@dataclass(kw_only=True)
class Model:
    id: UUID = Frozen(None)

    def __post_init__(self):
        self._id = self._id if self._id else uuid4()
