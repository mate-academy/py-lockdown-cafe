from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        vaccine = visitor["vaccine"]
        expiration_date = vaccine.get("expiration_date")

        if expiration_date is None:
            raise OutdatedVaccineError("Vaccine expiration date is missing")

        if isinstance(expiration_date, str):
            expiration_date = date.fromisoformat(expiration_date)

        if expiration_date < date.today():
            raise OutdatedVaccineError("Vaccine is outdated")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
