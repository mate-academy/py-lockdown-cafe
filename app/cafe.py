import datetime
from typing import Dict, Any

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
    InvalidVaccineDataError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict[str, Any]) -> str:
        """Validate visitor and return welcome string if allowed."""
        name = visitor.get("name", "Unknown")

        vaccine = visitor.get("vaccine")
        if vaccine is None:
            raise NotVaccinatedError(name)
        if not isinstance(vaccine, dict):
            raise InvalidVaccineDataError(name, "vaccine must be a dict")

        if "expiration_date" not in vaccine:
            raise InvalidVaccineDataError(name, "missing 'expiration_date'")

        expiration = vaccine["expiration_date"]
        if not isinstance(expiration, datetime.date):
            raise InvalidVaccineDataError(
                name, "'expiration_date' must be a datetime.date"
            )

        today = datetime.date.today()
        if expiration < today:
            raise OutdatedVaccineError(name, expiration)

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(name)

        return f"Welcome to {self.name}"
