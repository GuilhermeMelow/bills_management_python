from dataclasses import dataclass
from datetime import datetime

from src.Models.Amount import Amount
from src.Models.Model import Model


@dataclass
class Bill(Model):
    description: str
    due_date: datetime
    price: Amount
