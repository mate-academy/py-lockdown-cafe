import datetime
from typing import Dict
from .errors import (NotVaccinatedError,
                     OutdatedVaccineError,
                     NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict[str, any]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor must be vaccinated to enter.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is expired.")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor must wear a mask to enter.")
        return f"Welcome to {self.name}"
