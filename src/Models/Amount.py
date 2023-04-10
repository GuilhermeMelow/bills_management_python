class Amount(float):
    def __add__(self, __value: float) -> float:
        if __value <= 0:
            raise ValueError("Value passed for amount must be more than zero.")

        return super().__add__(__value)

    def __sub__(self, __value: float) -> float:
        copiedValue = float(self)
        sub_value = copiedValue - abs(__value)

        if sub_value < 0:
            raise ValueError("The Amount can't be negative.")

        return super().__sub__(__value)
