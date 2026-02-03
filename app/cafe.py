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
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You are not vaccinated")
        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Your vaccine outdated")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("You are not wearing mask")
        return f"Welcome to {self.name}"
