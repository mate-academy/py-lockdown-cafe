import datetime

from app.errors import (
    OutdatedVaccineError,
    NotVaccinatedError,
    NotWearingMaskError
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You must be a vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("You must update you vaccine")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("you must be wearing a mask")
        return f"Welcome to {self.name}"
