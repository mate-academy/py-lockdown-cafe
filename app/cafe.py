import datetime
from app.errors import (
    NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor is not vaccinated.")
        else:
            if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
                raise OutdatedVaccineError("Vaccine has expired.")
            elif not visitor["wearing_a_mask"]:
                raise NotWearingMaskError("The visitor does not have a mask.")
            return f"Welcome to {self.name}"
