from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor must be vaccinated.")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date and expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated.")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor must wear a mask.")

        return f"Welcome to {self.name}"
