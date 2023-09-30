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
        vaccine = visitor.get("vaccine")
        if vaccine is None:
            raise NotVaccinatedError("Visitor is not vaccinated.")
        if vaccine.get("expiration_date") < datetime.datetime.now().date():
            raise OutdatedVaccineError("Vaccine has expired")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor is not wearing a mask.")
        return f"Welcome to {self.name}"
