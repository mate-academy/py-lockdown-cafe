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
        current_date = date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You must to be vaccinated!")
        elif visitor["vaccine"]["expiration_date"] < current_date:
            raise OutdatedVaccineError("Your vaccine is expired. Do it again!")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You must wear a mask!")
        return f"Welcome to {self.name}"
