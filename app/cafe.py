import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name = visitor.get("name", "Visitor")

        vaccine = visitor.get("vaccine")
        if not isinstance(vaccine, dict):
            raise NotVaccinatedError(f"{name} is not vaccinated.")

        expiration_date = vaccine.get("expiration_date")
        if not isinstance(expiration_date, datetime.date):
            raise NotVaccinatedError(f"{name} is not vaccinated.")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(f"{name} has an outdated vaccine.")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{name} is not wearing a mask.")

        return f"Welcome to {self.name}"
