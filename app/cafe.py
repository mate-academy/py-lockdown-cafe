import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        # Check if vaccinated
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor["name"]} is not vaccinated.")

        # Check if vaccine is not outdated
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor["name"]}'s vaccine is outdated."
            )

        # Check if wearing a mask
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{visitor["name"]} is not wearing a mask."
            )

        # All checks passed
        return f"Welcome to {self.name}"
