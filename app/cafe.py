import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    """Represents a cafe enforcing pandemic entry rules."""

    def __init__(self, name: str) -> None:
        self.name: str = name

    def visit_cafe(self, visitor: dict) -> str:
        """Checks if the visitor can enter the cafe."""
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor must be vaccinated.")

        vaccine_info = visitor["vaccine"]
        expiration_date = vaccine_info.get("expiration_date")

        if not isinstance(expiration_date, datetime.date):
            raise OutdatedVaccineError("Invalid vaccine expiration date.")

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor must wear a mask.")

        return f"Welcome to {self.name}"
