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

        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor should be vaccinated.")

        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("Out dated vaccine")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Please, buy mask")

        return f"Welcome to {self.name}"
