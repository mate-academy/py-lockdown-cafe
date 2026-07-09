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
            raise NotVaccinatedError(visitor)

        expiration_date: datetime.date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(visitor)

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(visitor)

        return f"Welcome to {self.name}"
