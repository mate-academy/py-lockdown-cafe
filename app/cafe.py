from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You are not vaccinated!")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Your vaccine is expired!")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("You must wear a mask to enter the cafe.")
        else:
            return f"Welcome to {self.name}"
