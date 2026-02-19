from datetime import datetime

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
            raise NotVaccinatedError("Where is vaccine?")
        elif ("expiration_date" not in visitor["vaccine"]
              or visitor["vaccine"]["expiration_date"]
              < datetime.today().date()):
            raise OutdatedVaccineError("When do you get vaccine?")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Where is your mask?")
        return f"Welcome to {self.name}"
