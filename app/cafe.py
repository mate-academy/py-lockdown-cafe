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
            raise NotVaccinatedError("You need to be vaccinated!")
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Your date of vaccine is expired!")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You don't have mask!")
        return f"Welcome to {self.name}"
