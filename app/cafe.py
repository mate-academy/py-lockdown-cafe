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
        if not ("vaccine" in visitor):
            raise NotVaccinatedError("Visitor is not vaccinated!")

        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated!")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor needs to buy a mask!")

        return f"Welcome to {self.name}"
