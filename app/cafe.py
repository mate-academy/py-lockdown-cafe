from app.errors import (OutdatedVaccineError,
                        NotVaccinatedError,
                        NotWearingMaskError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You are not vaccinated")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("You expiration date is past due")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Wear a mask")
        else:
            return f"Welcome to {self.name}"
