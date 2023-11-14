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
        if not (visitor.get("vaccine").get("expiration_date")
                >= datetime.date.today()):
            raise OutdatedVaccineError("Visitor should have a valid vaccine.")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor should wear a mask.")
        return f"Welcome to {self.name}"
