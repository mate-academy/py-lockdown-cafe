import datetime
from typing import Any, Dict
from app.errors import (
    NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def visit_cafe(self, visitor: Dict[str, Any]) -> str:
        # Check if the visitor is vaccinated.
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor must be vaccinated")

        # Check if the vaccine is expired.
        vaccine_info = visitor["vaccine"]
        expiration_date = vaccine_info.get("expiration_date")
        if expiration_date is None or expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine has expired")

        # Check if the visitor is wearing a mask.
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor must wear a mask")

        return f"Welcome to {self.name}"
