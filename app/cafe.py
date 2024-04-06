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
        current_date = datetime.datetime.today().date()

        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor is not vaccinated.")

        if visitor["vaccine"]["expiration_date"] < current_date:
            raise OutdatedVaccineError("Vaccine is expired.")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
