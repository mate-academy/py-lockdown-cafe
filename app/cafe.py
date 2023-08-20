import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = datetime.date.today()

        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor is not vaccinated.")

        if visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError("Visitor's vaccine is outdated.")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor is not wearing mask.")

        return f"Welcome to {self.name}"
