from errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "Visitor must be vaccinated to visit the cafe"
            )
        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError(
                "Vaccine is expired"
            )
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                "Visitor must have a mask"
            )
        else:
            return f"Welcome to {self.name}"
