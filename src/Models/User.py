from dataclasses import dataclass
from uuid import UUID
from src.Models.Model import Model


@dataclass(kw_only=True, frozen=True)
class Person(Model):
    name: str
    email: str
    amount: float
    family_id: UUID


@dataclass(kw_only=True, frozen=True)
class Family(Model):
    description: str
