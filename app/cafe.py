from typing import TypedDict, NotRequired
from datetime import date

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Vaccine(TypedDict):
    expiration_date: date


class Visitor(TypedDict):
    name: str
    age: NotRequired[int]
    vaccine: NotRequired[Vaccine]
    wearing_a_mask: bool


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Visitor) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("The vaccine is outdated")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor is not wearing mask")
        return f"Welcome to {self.name}"
