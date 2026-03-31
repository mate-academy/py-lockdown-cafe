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
            raise NotVaccinatedError("Everybody must be vaccinated!")

        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Outdated vaccination!")

        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Everybody must be wearing a mask!")

        return f"Welcome to {self.name}"
