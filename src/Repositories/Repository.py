from typing import Generic, TypeVar
from uuid import UUID

from src.Services.Database import get_database
from src.Services.Mapper import Mapper


TDbModel = TypeVar("TDbModel")
TModel = TypeVar("TModel")


class Repository(Generic[TDbModel, TModel]):
    def __init__(self, collection_name: str, mapper: Mapper[TDbModel, TModel]):
        self._collection = get_database().get_collection(collection_name)
        self.mapper = mapper

    def list(self) -> list[TModel]:
        return [self.mapper.map(**m) for m in self._collection.find()]

    def add(self, data: TModel):
        db_model = self.mapper.map_invert(data)

        self._collection.insert_one(db_model.__dict__)

    def remove(self, id: UUID):
        self._collection.delete_one({"_id": id})

    def find(self, id: UUID):
        result = TDbModel(**self._collection.find_one({"_id": id}))

        return self.mapper.map(result)

    def update(self, id: UUID, data: TModel):
        db_model = self.mapper.map_invert(data)

        self._collection.update_one(
            filter={"_id": id},
            update={
                '$set': db_model.__dict__
            }
        )
