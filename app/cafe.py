import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        current_date = datetime.date.today()
        if visitor["vaccine"]["expiration_date"] < current_date:
            raise OutdatedVaccineError("Visitor should do a new vaccine")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor must buy a mask")
        return f"Welcome to {self.name}"
