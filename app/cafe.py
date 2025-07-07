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
        vaccine = visitor.get("vaccine", 0)
        if not vaccine:
            raise NotVaccinatedError("Visitor does not have vaccine")
        elif vaccine["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is expired")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("User does not have mask")
        else:
            return f"Welcome to {self.name}"
