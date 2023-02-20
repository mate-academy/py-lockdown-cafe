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
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor is not vaccinated!")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The vaccine is outdated!")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Not wearing mask! Must have one!")
        return f"Welcome to {self.name}"
