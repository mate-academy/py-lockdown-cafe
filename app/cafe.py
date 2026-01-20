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
            raise NotVaccinatedError("It is necessary to get vaccinated.")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The vaccine is expired.")
        elif not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("There is no medical mask")
        else:
            return f"Welcome to {self.name}"
