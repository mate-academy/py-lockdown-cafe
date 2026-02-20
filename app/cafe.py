import datetime
from .errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)
from typing import Dict, Any


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict[str, Any]) -> str:
        vaccine_data = visitor.get("vaccine")
        if not isinstance(vaccine_data, dict):
            raise NotVaccinatedError("Visitor must be vaccinated to enter")

        expiration_date = vaccine_data.get("expiration_date")
        if not isinstance(expiration_date, datetime.date):
            raise OutdatedVaccineError("Invalid or missing expiration date")

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is expired")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor must wear a mask to enter")

        return f"Welcome to {self.name}"
