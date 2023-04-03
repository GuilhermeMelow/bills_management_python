import math
from src.Utils.Frozen import Frozen


from dataclasses import dataclass


@dataclass
class Amount():
    value: float = Frozen()

    def increase(self, value):
        if value <= 0:
            raise ValueError("Value must more than zero.")

        self._value += value

    def decrease(self, value):
        sub_value = self._value - abs(value)

        if sub_value < 0:
            raise ValueError("The value can't be negative.")

        self._value = sub_value
