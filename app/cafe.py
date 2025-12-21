from app.errors import (
    NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError)
from datetime import date


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor must be vaccinated")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("The vaccine is expired")
        if "wearing_a_mask" not in visitor:
            raise NotWearingMaskError("Visitor must wear mask")
        else:
            if not visitor["wearing_a_mask"]:
                raise NotWearingMaskError("Visitor must wear mask")
        return f"Welcome to {self.name}"
