from typing import Optional, TypedDict

from app.models.vaccine import Vaccine


class Visitor(TypedDict):
    name: str
    age: int
    vaccine: Optional[Vaccine]
    wearing_a_mask: Optional[bool]
