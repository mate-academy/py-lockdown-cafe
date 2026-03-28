from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
from datetime import date


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")

        if not isinstance(visitor["vaccine"], dict):
            raise OutdatedVaccineError("Vaccine data is invalid.")

        if "expiration_date" not in visitor["vaccine"]:
            raise OutdatedVaccineError("Vaccine expiration date is missing.")

        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Vaccine is outdated.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
