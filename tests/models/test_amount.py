import unittest
from datetime import datetime
from src.Models.Amount import Amount

from src.Models.Bill import Bill


class BillTest(unittest.TestCase):
    def test_create_amount(self):
        amount_value = 10

        amount = Amount(amount_value)

        self.assertEqual(amount.value, amount_value)

    def test_increase_amount(self):
        amount_value = 10
        result = 30
        amount = Amount(amount_value)

        amount.increase(20)

        self.assertEqual(amount.value, result)

    def test_decrease_amount(self):
        amount_value = 30
        result = 10
        amount = Amount(amount_value)

        amount.decrease(20)

        self.assertEqual(amount.value, result)

    def test_increase_exception(self):
        amount_increase_value = -20

        amount = Amount(20)

        self.assertRaises(ValueError, amount.increase, amount_increase_value)

    def test_decrease_exception(self):
        amount_decrease_value = -20

        amount = Amount(0)

        self.assertRaises(ValueError, amount.decrease, amount_decrease_value)


if __name__ == '__main__':
    unittest.main()
