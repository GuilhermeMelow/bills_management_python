from datetime import datetime
from uuid import UUID

from src.Models.Bill import Bill


class BillRepository:
    _bills: list[Bill] = [
        Bill("Teste", datetime.now())
    ]

    def list(self):
        return self._bills

    def add(self, bill: Bill):
        self._bills.append(bill)

    def remove(self, bill_id: UUID):
        bill = self.find(bill_id)

        self._bills.remove(bill)

    def find(self, bill_id: UUID):
        result = next((bill for bill in self._bills if bill_id == bill.id), None)

        return result

    def update(self, bill):
        old_bill = self.find(bill.id)
        index = self._bills.index(old_bill)

        self._bills[index] = bill
