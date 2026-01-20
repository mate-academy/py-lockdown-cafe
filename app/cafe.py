from datetime import date

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if "vaccine" not in visitor:
            raise NotVaccinatedError("You don't have vaccine")

        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Your vaccine is out of date")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("YOU DON'T HAVE MASK!!!")

        return f"Welcome to {self.name}"
