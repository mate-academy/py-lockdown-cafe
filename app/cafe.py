import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if not visitor.get("vaccine", False):
            raise NotVaccinatedError("Visitor is not vaccinated")

        vaccine_date = visitor.get("vaccine").get("expiration_date")
        if vaccine_date and vaccine_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
