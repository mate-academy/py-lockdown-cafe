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
        vaccine = visitor.get("vaccine")
        if vaccine is None:
            raise NotVaccinatedError("Visitor should have vaccine")
        current_date = date.today()
        exp_date = vaccine["expiration_date"]
        if exp_date < current_date:
            raise OutdatedVaccineError("Visitor has expired vaccine")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor isn't wearing mask")
        return f"Welcome to {self.name}"
