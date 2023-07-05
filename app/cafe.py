from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError)
from datetime import date


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("The visitor's  vaccine is expired")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor must wear mask")
        return f"Welcome to {self.name}"
