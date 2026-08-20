import datetime
from app.errors import (
    OutdatedVaccineError,
    NotVaccinatedError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("You must be vaccinated!")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Your vaccine has expired!")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Please put your mask on your face!")
        return f"Welcome to {self.name}"
