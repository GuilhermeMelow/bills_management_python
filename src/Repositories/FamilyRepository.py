from dataclasses import dataclass
from uuid import UUID
from src.DbModels.Bill import DbModel
from src.Models.User import Family
from src.Repositories.Repository import Repository


class FamilyRepository(Repository[Family]):
    def __init__(self):
        super().__init__("family")


@dataclass
class FamilyDbModel(DbModel):
    _id: UUID
    description: str
    persons: list[UUID]
