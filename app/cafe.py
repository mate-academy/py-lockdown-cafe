from app.errors import (OutdatedVaccineError,
                        NotVaccinatedError,
                        NotWearingMaskError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("You expiration date is past due")
            if not visitor["wearing_a_mask"]:
                raise NotWearingMaskError("Wear a mask")
        except KeyError:
            raise NotVaccinatedError("You are not vaccinated")
        else:
            return f"Welcome to {self.name}"
