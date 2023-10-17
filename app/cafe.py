from datetime import date

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You need a vaccination!")
        relevant_date = visitor["vaccine"].get("expiration_date")
        if relevant_date < date.today():
            raise OutdatedVaccineError("Your vaccination is overdue!")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("A mask is required to enter!")
        return f"Welcome to {self.name}"
