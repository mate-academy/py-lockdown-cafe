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
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is missing a vaccine")
        elif datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("Visitor's vaccine is outdated")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor is missing a mask")
        return f"Welcome to {self.name}"
