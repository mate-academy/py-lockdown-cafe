from __future__ import annotations
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
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "Visitor is not vaccinated and "
                "therefore cannot enter the cafe."
            )

        vaccine = visitor["vaccine"]

        if vaccine["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "Visitor's vaccine is expired and they need to get a new one."
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                "Visitor is not wearing a mask and "
                "must wear one to enter the cafe."
            )

        return f"Welcome to {self.name}"
