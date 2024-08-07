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

        if not visitor.get("vaccine"):
            raise NotVaccinatedError("The visitor doesn't have a vaccine")

        elif visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("The visitor's vaccine is outdated!")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("The visitor doesn't have a mask!")

        return f"Welcome to {self.name}"
