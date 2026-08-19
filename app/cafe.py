from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("This visitor is not vaccinated!")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("This visitor's vaccine is outdated!")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("This visitor isn't wearing a mask")
        return f"Welcome to {self.name}"
