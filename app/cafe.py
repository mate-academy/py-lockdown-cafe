from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
from datetime import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Visitor is not vaccinated.")
        elif visitor["vaccine"]["expiration_date"] < datetime.now().date():
            raise OutdatedVaccineError("Visitor's vaccine is expired.")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor is not wearing a mask.")
        else:
            return f"Welcome to {self.name}"
