import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> str:
        self.name = name

    def visit_cafe(self, visitor: str) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date and expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is expired.")
        if not visitor.get("wearing_a_mask", True):
            raise NotWearingMaskError("Visitor is not wearing a mask.")
        return f"Welcome to {self.name}"
