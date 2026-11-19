import datetime
from typing import TypedDict

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class VaccineInfo(TypedDict):
    expiration_date: datetime.date


class Visitor(TypedDict, total=False):
    name: str
    age: int
    vaccine: VaccineInfo
    wearing_a_mask: bool


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Visitor) -> str:
        if "vaccine" in visitor.keys():
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("The vaccine has expired")
        else:
            raise NotVaccinatedError("The visitor is not vaccinated")
        if ("wearing_a_mask" not in visitor.keys()
                or visitor["wearing_a_mask"] is False):
            raise NotWearingMaskError("The visitor is not wearing a mask")
        return f"Welcome to {self.name}"
