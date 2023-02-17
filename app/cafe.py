import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> [str, Exception]:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Only vaccinated customers allowed")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Your vaccine expired")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("You need to wear a mask")
        return f"Welcome to {self.name}"
