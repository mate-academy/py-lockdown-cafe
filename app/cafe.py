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
        if (
            visitor.get("vaccine") is None
            or "expiration_date" not in visitor["vaccine"]
        ):
            raise NotVaccinatedError("Visitor does not have vaccine")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is expired")
        elif not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("User does not have mask")
        return f"Welcome to {self.name}"
