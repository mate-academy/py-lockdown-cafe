import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine has expired.")
        if not visitor.get("wearing_a_mask", True):
            raise NotWearingMaskError("Visitor is not wearing a mask.")
        else:
            return f"Welcome to {self.name}"
