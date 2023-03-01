import unittest
from datetime import datetime

from src.Models.Bill import Bill
from src.Repositories.BillRepository import BillRepository


class BillRepositoryTest(unittest.TestCase):
    def test_add(self):
        repository = BillRepository()
        bill = Bill("Teste", datetime.now(), 100)

        repository.add(bill)

        bills = repository.list()
        self.assertDictEqual(bills[0].__dict__, bill.__dict__)

    def test_find(self):
        repository = BillRepository()
        bill = Bill("TesteFind", datetime(2022, 12, 10), 100)
        repository.add(bill)

        result = repository.find(bill.id)

        self.assertDictEqual(result.__dict__, bill.__dict__)

    def test_remove(self):
        repository = BillRepository()
        bill = Bill("TesteRemove", datetime(2022, 12, 10), 100)
        repository.add(bill)

        repository.remove(bill.id)

        result = repository.find(bill.id)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
