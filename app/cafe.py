from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
from datetime import date

class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")

        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("The visitor is out of date vaccinated.")

        elif not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("A visitor without a mask.")

        else:
            return f"Welcome to {self.name}"
