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
        count_err = 0
        if "vaccine" not in visitor:
            count_err += 1
            raise NotVaccinatedError("Visitor is not vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            count_err += 1
            raise OutdatedVaccineError("The vaccine is expired")
        if "wearing_a_mask" not in visitor or not visitor["wearing_a_mask"]:
            count_err += 1
            raise NotWearingMaskError("Visitor is not wearing the mask")
        if not count_err:
            return f"Welcome to {self.name}"
