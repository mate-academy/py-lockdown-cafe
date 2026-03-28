import datetime

from app.errors import (
NotVaccinatedError,
OutdatedVaccineError,
NotWearingMaskError
)
class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not "vaccine" in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"Vaccine is expired on {visitor['vaccine']['expiration_date']}")
        if visitor.get("wearing_a_mask") is not True:
            raise NotWearingMaskError("Visitor is not wearing a mask")
        return f"Welcome to {self.name}"
