from ctypes import Union
from uuid import UUID, uuid4
from datetime import datetime


class Bill:
    def __init__(self, description: str, due_date: datetime, price: float, id: Union[UUID, None] = None):
        self.description = description
        self.due_date = due_date
        self.increase(price)
        self._id = id if id is not None else uuid4()

    _price = 0

    @property
    def price(self) -> float:
        return self._price

    @property
    def id(self) -> UUID:
        return self._id

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
