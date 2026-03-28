import datetime

from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        if not vaccine or "expiration_date" not in vaccine:
            raise NotVaccinatedError("NotVaccinatedError")

        if vaccine["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")

        if visitor.get("wearing_a_mask") is not True:
            raise NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"
