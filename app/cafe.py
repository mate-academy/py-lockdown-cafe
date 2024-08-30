import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("The visitor must have the vaccine.")
        elif (visitor.get("vaccine")
                     .get("expiration_date") < datetime.date.today()):
            raise OutdatedVaccineError("The vaccine expired.")
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("The visitor must have a mask.")
        return f"Welcome to {self.name}"
