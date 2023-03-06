from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(init=True)
class BillDbModel:
    _id: UUID
    description: str
    due_date: datetime
    _price: float

    def __post_init__(self):
        privates = [field for field in self.__dict__ if field[0] is '_']

        for field in privates:
            setattr(self, field[1:], getattr(self, field))
            delattr(self, field)
