import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        # Check if the visitor is vaccinated
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")

        # Check if the vaccine is not expired
        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated.")

        # Check if the visitor is wearing a mask
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        # All conditions are met
        return f"Welcome to {self.name}"
