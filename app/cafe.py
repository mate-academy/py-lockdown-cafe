from datetime import date
from typing import Dict, Any
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict[str, Any]) -> str:
        """Validate visitor and return welcome message or raise error."""
        vaccine = visitor.get("vaccine")

        if vaccine is None:
            raise NotVaccinatedError("Visitor has no vaccine")

        if vaccine["expiration_date"] < date.today():
            raise OutdatedVaccineError("Vaccine is outdated")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
