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
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Should be vaccinated!")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Your vaccine is expired!")
        if visitor["wearing_a_mask"] is not True:
            raise NotWearingMaskError("You must wear a mask!")
        return f"Welcome to {self.name}"
