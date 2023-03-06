from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from dateutil.parser import parse


@dataclass(init=True)
class BillRequest:
    id: UUID
    description: str
    due_date: datetime
    price: float

    @classmethod
    def create(cls, dct: dict[str, str], bill_id=None):
        return BillRequest(description=dct["description"],
                           price=float(dct["price"]),
                           due_date=parse(dct["due_date"]),
                           id=UUID(bill_id) if bill_id is not None else None)
