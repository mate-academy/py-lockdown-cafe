from datetime import date
from typing import Any

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def visit_cafe(self, visitor: dict[str, Any]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Go get vaccine!")

        expiry_date: date = visitor["vaccine"]["expiration_date"]

        if expiry_date < date.today():
            raise OutdatedVaccineError("Go for next dose")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Grab some mask")

        return f"Welcome to {self.name}"
