import datetime
from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("Someone is not vaccinated!")
        if visitor.get("vaccine").\
                get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError(
                "Expiration date if vaccine is expired!")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("You can't go in without mask!")
        return f"Welcome to {self.name}"
