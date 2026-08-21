import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> str:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You are not vaccinated!")
        date = datetime.date.today()
        if date > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("Your vaccine is over!")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("You don't have a mask!")

        return f"Welcome to {self.name}"
