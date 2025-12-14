import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        current_date = datetime.date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")
        if visitor["vaccine"]["expiration_date"] < current_date:
            raise OutdatedVaccineError("expired vaccine")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Need a wearing mask")

        return f"Welcome to {self.name}"
