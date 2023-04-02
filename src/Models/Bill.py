from dataclasses import dataclass
from uuid import UUID, uuid4
from datetime import datetime

from src.Models.Model import Model


@dataclass(kw_only=True, frozen=True)
class Bill(Model):
    description: str
    due_date: datetime
    price = 0.0

    def increase(self, value: float):
        if value <= 0:
            raise ValueError("Value must more than zero.")

        self._price += value

    def decrease(self, value: float):
        if value < 0:
            raise ValueError("Value must be positive.")

        price = self.price - value

        if price < 0:
            raise ValueError("The price can't be negative.")

        self._price = price
