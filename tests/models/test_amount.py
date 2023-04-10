import unittest
from datetime import datetime
from src.Models.Amount import Amount

from src.Models.Bill import Bill


class BillTest(unittest.TestCase):
    def test_create_amount(self):
        amount_value = 10

        amount = Amount(amount_value)

        self.assertEqual(amount, amount_value)

    def test_increase_amount(self):
        amount_value = 10
        add_value = 20
        result = 30
        amount = Amount(amount_value)

        amount += add_value

        self.assertEqual(amount, result)

    def test_decrease_amount(self):
        amount_value = 30
        sub_value = 20
        result = 10
        amount = Amount(amount_value)

        amount -= sub_value

        self.assertEqual(amount, result)

    def test_increase_exception(self):
        amount = Amount(20)

        def increase_exception(amount, value=-20): amount += value

        self.assertRaises(ValueError, increase_exception, amount)

    def test_decrease_exception(self):
        amount = Amount(0)

        def decrease_exception(amount, value=-20): amount -= value

        self.assertRaises(ValueError, decrease_exception, amount)


if __name__ == '__main__':
    unittest.main()
