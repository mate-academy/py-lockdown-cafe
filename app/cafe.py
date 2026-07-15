from datetime import date
from app.errors import (
    OutdatedVaccineError,
    NotVaccinatedError,
    NotWearingMaskError)


current_date = date.today()


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor must be vaccinated")
        if visitor["vaccine"]["expiration_date"] < current_date:
            raise OutdatedVaccineError("Visitor vaccine has expired")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Friend must wear mask")
        return f"Welcome to {self.name}"
