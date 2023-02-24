from datetime import datetime
from src.Models.Bill import Bill
from src.Repositories.BillRepository import BillRepository

if __name__ == '__main__':
    bill = Bill.create_with_price("", datetime(2022, 12, 10), 120)

    repository = BillRepository()
    repository.add(bill)
    repository.update(Bill("Test", bill.due_date, bill.id))

    print(repository.find(bill.id).description)
