from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from src.Models.Bill import Bill


@dataclass(init=True)
class BillResponse:
    id: UUID
    description: str
    due_date: datetime
    price: float = 0

    @classmethod
    def create(cls, bill: Bill):
        result = cls(bill.id, bill.description, bill.due_date, bill.price)

        return result.__dict__
