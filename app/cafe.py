from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"The visitor {visitor['name']} "
                                     f"is not vaccinated.")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The vaccine has expired.")
        elif ("wearing_a_mask" not in visitor
              or visitor["wearing_a_mask"] is False):
            raise NotWearingMaskError("Wear a mask!")
        else:
            return f"Welcome to {self.name}"
