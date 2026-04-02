from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    """Represents a cafe that visitors can enter if they meet the rules."""

    def __init__(self, name: str) -> None:
        """Initializes the cafe with a given name."""
        self.name = name

    def visit_cafe(self, visitor: dict[str, object]) -> str:
        """Checks if a visitor meets all conditions to enter the cafe.

        Raises:
            NotVaccinatedError: If the visitor is not vaccinated.
            OutdatedVaccineError: If the vaccine has expired.
            NotWearingMaskError: If the visitor is not wearing a mask.

        Returns:
            str: A welcome message if the visitor meets all conditions.
        """
        vaccine_info = visitor.get("vaccine")

        if not isinstance(vaccine_info, dict):
            raise NotVaccinatedError("Visitor is not vaccinated.")

        expiration_date = vaccine_info.get("expiration_date")

        if not isinstance(expiration_date, date):
            raise OutdatedVaccineError("Invalid vaccine expiration date.")
        if expiration_date < date.today():
            raise OutdatedVaccineError("Vaccine has expired.")

        if visitor.get("wearing_a_mask") is not True:
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
