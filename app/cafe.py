from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("You must be vaccinated!")

        visitor_date = visitor["vaccine"]["expiration_date"]
        today = date.today()
        if visitor_date < today:
            raise OutdatedVaccineError("Your vaccine is outdated!")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("You should wear some mask!")

        return f"Welcome to {self.name}"
