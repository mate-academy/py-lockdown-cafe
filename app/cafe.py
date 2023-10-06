import datetime

from app.errors import (
    NotWearingMaskError,
    OutdatedVaccineError,
    NotVaccinatedError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        error = 0
        if "vaccine" not in visitor:
            error += 1
            raise NotVaccinatedError("Visitor has to be vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine expired")
        if visitor["wearing_a_mask"] is False:
            error += 1
            raise NotWearingMaskError("Visitor without a mask")
        if error == 0:
            return f"Welcome to {self.name}"
