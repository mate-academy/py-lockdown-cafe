from datetime import date

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You have to be vaccinated to visit cafe")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("The vaccine must not be expired")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("You have to wear a mask")
        return f"Welcome to {self.name}"
