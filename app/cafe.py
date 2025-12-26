from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        current_day = datetime.date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")
        elif visitor["vaccine"]["expiration_date"] < current_day:
            raise OutdatedVaccineError("Vaccine is expired.")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor is not wearing a mask.")
        return f"Welcome to {self.name}"
