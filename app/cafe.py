import datetime
from app.errors import (
    VaccineError,
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)

class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor must be vaccinated to enter.")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine has expired.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor must wear a mask.")

        return f"Welcome to {self.name}"
