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
        vaccine = visitor.get("vaccine")
        if not vaccine:
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_date = vaccine.get("expiration_date")
        if expiration_date and expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated.")

        if not visitor.get("wearing_a_mask", None):
            raise NotWearingMaskError("Visitor is not wearing the mask")

        return f"Welcome to {self.name}"
