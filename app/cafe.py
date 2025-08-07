# app/cafe.py

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
        name = visitor.get("name", "Visitor")
        vaccine = visitor.get("vaccine")
        if vaccine is None:
            raise NotVaccinatedError(
                f"{name} must be vaccinated to enter {self.name}"
            )

        exp_date = vaccine.get("expiration_date")
        if not isinstance(exp_date, date) or exp_date < date.today():
            raise OutdatedVaccineError(
                f"Vaccine for {name} is expired as of {exp_date}"
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{name} must wear a mask to enter {self.name}"
            )

        return f"Welcome to {self.name}"
