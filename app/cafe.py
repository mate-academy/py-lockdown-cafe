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
        if "vaccine" in visitor:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("Your vaccine is out of date")
            if not visitor["wearing_a_mask"]:
                raise NotWearingMaskError("You should wear mask")
            return f"Welcome to {self.name}"
        else:
            raise NotVaccinatedError("All friends should be vaccinated")
