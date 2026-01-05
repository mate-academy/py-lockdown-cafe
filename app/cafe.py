import datetime

import app.errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        """Validates visitor information without printing anything."""

        # Check vaccine presence
        vaccine = visitor.get("vaccine")
        if vaccine is None:
            raise app.errors.NotVaccinatedError(
                f"{visitor['name']} is not vaccinated."
            )

        # Check expiration date
        expiration = vaccine.get("expiration_date")
        if expiration is None:
            raise app.errors.NotVaccinatedError(
                f"{visitor['name']} has no expiration date for the vaccine."
            )

        if expiration < datetime.date.today():
            raise app.errors.OutdatedVaccineError(
                f"{visitor['name']}'s vaccine has expired on {expiration}."
            )

        # Check mask
        if not visitor.get("wearing_a_mask", False):
            raise app.errors.NotWearingMaskError(
                f"{visitor['name']} is not wearing a mask."
            )

        return f"Welcome to {self.name}"
