from uuid import UUID

from src.DbModels.Bill import BillDbModel
from src.Models.Bill import Bill
from src.Services.Database import get_database


class BillRepository:
    __db = get_database()
    __collection = __db.get_collection("bills")

    def list(self):
        db_models = [BillDbModel(**m) for m in self.__collection.find()]

        return [Bill(**m.__dict__) for m in db_models]

    def add(self, bill: Bill):
        self.__collection.insert_one(bill.__dict__)

    def remove(self, bill_id: UUID):
        self.__collection.delete_one({"_id": bill_id})

    def find(self, bill_id: UUID) -> Bill:
        db_model = BillDbModel(**self.__collection.find_one({"_id": bill_id}))

        return Bill(**db_model.__dict__)

    def update(self, bill_id: UUID, bill: Bill):
        self.__collection.update_one(
            filter={"_id": bill_id},
            update={
                '$set': bill.__dict__
            }
        )
