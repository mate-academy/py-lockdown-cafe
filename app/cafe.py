import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "Visitor must be vaccinated before entering the cafe"
            )

        vaccine = visitor["vaccine"]
        expiration_date = vaccine.get("expiration_date")
        if expiration_date is None:
            raise NotVaccinatedError(
                "Visitor must be vaccinated before entering the cafe"
            )

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine has expired")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor must wear a mask")

        return f"Welcome to {self.name}"
