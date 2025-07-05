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
        if not visitor.get("vaccine", False):
            raise NotVaccinatedError(
                "Visitor must present a valid vaccination record."
            )
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(
                "Visitor's vaccine is expired and no longer valid."
            )
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                "Visitor is not wearing a protective mask."
            )
        return f"Welcome to {self.name}"
