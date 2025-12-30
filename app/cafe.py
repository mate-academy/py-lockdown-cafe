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
        today = date.today()

        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("You should be vaccinated!")
        elif visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError("Your vaccine is outdated!")
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("You should wear a mask!")

        return f"Welcome to {self.name}"
