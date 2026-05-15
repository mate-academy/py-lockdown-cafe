import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    """A cafe that enforces pandemic safety rules."""

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        """Allow a visitor to enter the cafe if they meet all safety
        requirements.

        Args:
            visitor: A dictionary containing visitor information
                    including 'vaccine' and 'wearing_a_mask' keys.

        Returns:
            A welcome message if all requirements are met.

        Raises:
            NotVaccinatedError: If the visitor doesn't have a vaccine.
            OutdatedVaccineError: If the visitor's vaccine has expired.
            NotWearingMaskError: If the visitor is not wearing a mask.
        """
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "Visitor must be vaccinated to enter the cafe."
            )

        vaccine = visitor["vaccine"]
        if "expiration_date" not in vaccine:
            raise NotVaccinatedError(
                "Vaccine must have an expiration date."
            )

        expiration_date = vaccine["expiration_date"]
        today = datetime.date.today()

        if expiration_date < today:
            raise OutdatedVaccineError("Visitor's vaccine has expired.")

        if "wearing_a_mask" not in visitor or not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                "Visitor must wear a mask to enter the cafe."
            )

        return f"Welcome to {self.name}"
