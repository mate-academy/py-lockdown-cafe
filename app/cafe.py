import datetime
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
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor.get('name', 'Visitor')} is not vaccinated"
            )

        vaccine = visitor["vaccine"]
        expiration_date = vaccine.get("expiration_date")
        if not isinstance(expiration_date, datetime.date):
            raise OutdatedVaccineError(
                "Invalid or missing vaccine expiration date"
            )

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is expired")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{visitor.get('name', 'Visitor')} is not wearing a mask"
            )

        return f"Welcome to {self.name}"
