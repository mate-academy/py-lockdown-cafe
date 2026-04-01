from typing import TypedDict
from app.models.vaccine import Vaccine


class Visitor(TypedDict):
    name: str
    age: int
    vaccine: Vaccine
    wearing_a_mask: bool
