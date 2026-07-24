import datetime
from datetime import date
from typing import TypedDict

from app.errors import (
    OutdatedVaccineError,
    NotWearingMaskError,
    NotVaccinatedError
)


class Visitor(TypedDict):
    name: str
    vaccine: date
    wearing_a_mask: bool


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Visitor) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(
                f"{visitor['name']} should be vaccinated"
            )
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor['name']} should renew his vaccine"
            )
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f"{visitor['name']} should wear a mask"
            )
        return f"Welcome to {self.name}"
