from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    """Represents a cafe with simple pandemic rules."""

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        """
        Validate a single visitor.

        Rules:
          1) Must have 'vaccine' with 'expiration_date' (date).
          2) expiration_date must be today or in the future.
          3) 'wearing_a_mask' must be True (missing key = no mask).

        Returns:
            str: "Welcome to {cafe.name}" when all checks pass.

        Raises:
            NotVaccinatedError: no vaccine info or invalid expiration_date.
            OutdatedVaccineError: vaccine is expired.
            NotWearingMaskError: visitor not wearing a mask.
        """
        vaccine = visitor.get("vaccine")
        if not vaccine:
            name = visitor.get("name")
            who = f" '{name}'" if name else ""
            raise NotVaccinatedError(f"Visitor{who} is not vaccinated.")

        exp = vaccine.get("expiration_date")
        if not isinstance(exp, date):
            raise NotVaccinatedError(
                "Vaccine 'expiration_date' must be a datetime.date."
            )

        if exp < date.today():
            raise OutdatedVaccineError(
                f"Vaccine expired on {exp.isoformat()}."
            )

        if visitor.get("wearing_a_mask") is not True:
            raise NotWearingMaskError("Mask is required to enter the cafe.")

        return f"Welcome to {self.name}"
