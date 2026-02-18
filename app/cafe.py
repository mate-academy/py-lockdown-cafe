from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        # Check if visitor has a name
        if "name" not in visitor:
            raise ValueError("Visitor must have a name")

        # Check if visitor is vaccinated
        if "vaccine" not in visitor:
            raise NotVaccinatedError(visitor["name"])

        # Check if vaccine is not expired
        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(visitor["name"])

        # Check if visitor is wearing a mask
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(visitor["name"])

        return f"Welcome to {self.name}"
