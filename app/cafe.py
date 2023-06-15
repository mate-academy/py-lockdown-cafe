from datetime import date

from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor don't have vaccine")
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor don't have a mask")
        return f"Welcome to {self.name}"
