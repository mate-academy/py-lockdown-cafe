from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Not vaccinated.")
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Outdated vaccine.")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Without mask.")

        return f"Welcome to {self.name}"
