from dataclasses import dataclass
from uuid import UUID

from src.Models.Amount import Amount
from src.Models.Model import Model


@dataclass
class Person(Model):
    name: str
    email: str
    family_id: UUID
    amount: Amount


@dataclass
class Family(Model):
    description: str
