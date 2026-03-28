import datetime
from typing import TypedDict

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Vaccine(TypedDict):
    expiration_date: datetime.date


class Visitor(TypedDict):
    name: str
    age: int
    vaccine: Vaccine
    wearing_a_mask: bool


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Visitor) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError
        elif (
            "wearing_a_mask" not in visitor
            or visitor["wearing_a_mask"] is False
        ):
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
