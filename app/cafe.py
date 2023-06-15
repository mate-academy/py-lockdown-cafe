from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor must be vaccinated!")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Visitor's vaccine must be up to date!")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor has to wear a mask!")
        return f"Welcome to {self.name}"
