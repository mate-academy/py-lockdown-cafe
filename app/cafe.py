import datetime as dt
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = dt.date.today()

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor must be vaccinated")
        elif today > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("Visitor's vaccination has expired")
        elif not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor must be wearing a mask")
        else:
            return f"Welcome to {self.name}"
