from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        wearing_a_mask = visitor.get("wearing_a_mask")

        if not vaccine:
            raise NotVaccinatedError("Visitor is not vaccinated.")

        expiration_date = vaccine.get("expiration_date")
        if expiration_date and expiration_date < date.today():
            raise OutdatedVaccineError("Visitor's vaccine has expired.")

        if not wearing_a_mask:
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
