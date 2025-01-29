from datetime import date
from typing import Dict, Any
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict[str, Any]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "Visitor must be vaccinated to enter the cafe.")

        vaccine_expiration = visitor["vaccine"]["expiration_date"]
        if vaccine_expiration < date.today():
            raise OutdatedVaccineError(
                "Visitor's vaccine has expired and is no longer valid.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                "Visitor must wear a mask to enter the cafe.")

        return f"Welcome to {self.name}"