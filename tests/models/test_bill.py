import unittest
from datetime import datetime

from src.Models.Bill import Bill


class BillTest(unittest.TestCase):
    def test_create_with_price(self):
        price = 120.22
        bill = Bill.create_with_price("Teste", datetime.now(), price)

        self.assertEqual(bill.price, price)

    def test_increase(self):
        increase_value = 100.20
        bill = Bill("Teste", datetime.now())

        bill.increase(increase_value)

        self.assertEqual(bill.price, increase_value)

    def test_increase_exception(self):
        decrease_value = -100.20
        bill = Bill("Teste", datetime.now())

        self.assertRaises(ValueError, bill.increase, decrease_value)

    def test_decrease(self):
        decrease_value = 100.20
        result = 20.00
        bill = Bill.create_with_price("Teste", datetime.now(), 120.20)

        bill.decrease(decrease_value)

        self.assertEqual(bill.price, result)

    def test_decrease_exception(self):
        decrease_value = -100.20
        bill = Bill("Teste", datetime.now())

        self.assertRaises(ValueError, bill.decrease, decrease_value)

    def test_decrease_zero_price_exception(self):
        bill = Bill.create_with_price("Teste", datetime.now(), 20)

        self.assertRaises(ValueError, bill.decrease, 100)


if __name__ == '__main__':
    unittest.main()
