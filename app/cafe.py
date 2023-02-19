import datetime
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:

        if not visitor.get("vaccine"):
            raise NotVaccinatedError("you are not vaccinated")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("your vaccine is expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("you are not wearing a mask")

        return f"Welcome to {self.name}"
