import datetime

from typing import Dict

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict) -> None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("visitor is not vaccinated.")
        expiration_date = visitor["vaccine"].get("expiration_date")
        if (not isinstance(expiration_date, datetime.date)
                or expiration_date < datetime.date.today()):
            raise OutdatedVaccineError("Visitor's vaccine is expired.")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask.")
        return (f"Welcome to {self.name}")
