"""Define a cafe and its visitor admission rules."""

import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    """Represent a cafe that validates visitors before admission."""

    def __init__(self, name: str) -> None:
        """Initialize a cafe with the given name."""
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        """Validate a visitor and allow them to enter the cafe."""
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_date = visitor["vaccine"]["expiration_date"]

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
