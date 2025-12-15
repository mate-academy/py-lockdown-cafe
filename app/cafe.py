from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name = visitor.get("name")

        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{name} is not vaccinated")

        vaccine = visitor.get("vaccine")
        expiration_date = vaccine.get("expiration_date")

        if expiration_date < date.today():
            raise OutdatedVaccineError(f"{name}'s vaccine is expired")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"{name} is not wearing a mask")

        return f"Welcome to {self.name}"
