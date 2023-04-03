from dataclasses import dataclass
from datetime import datetime

from src.Models.Model import Model
from src.Utils.Frozen import Frozen


@dataclass
class Bill(Model):
    description: str
    due_date: datetime
    price: float = Frozen()

    def increase(self, value: float):
        if value <= 0:
            raise ValueError("Value must more than zero.")

        self._price += value

    def decrease(self, value: float):
        if value < 0:
            raise ValueError("Value must be positive.")

        price = self._price - value

        if price < 0:
            raise ValueError("The price can't be negative.")

        self._price = price
