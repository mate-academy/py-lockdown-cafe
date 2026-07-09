import datetime
from typing import Any

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    """Cafe class with pandemic rules."""

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, Any]) -> str:
        """Check visitor rules before entering the cafe."""
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor['name']} is not vaccinated."
            )

        expiration_date: datetime.date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor['name']}'s vaccine is outdated."
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{visitor['name']} is not wearing a mask."
            )

        return f"Welcome to {self.name}"
