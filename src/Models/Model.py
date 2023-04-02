
from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(kw_only=True, frozen=True)
class Model:
    id: UUID

    def __post__init__(self):
        self._id = self.id if self.id else uuid4()
