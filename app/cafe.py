import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        if not vaccine:
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_date = vaccine.get("expiration_date")
        if expiration_date is None:
            raise OutdatedVaccineError("Vaccine expiration date is missing")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine has expired")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
