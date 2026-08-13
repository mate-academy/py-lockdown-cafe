from datetime import date
from .errors import (OutdatedVaccineError,
                     NotWearingMaskError,
                     NotVaccinatedError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "Visitor is not vaccinated")

        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated")

        if ("wearing_a_mask" not in visitor
                or visitor["wearing_a_mask"] is False):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
