import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Sorry, visitor is not vaccinated.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Sorry, visitor's vaccine is outdated.")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Please, wear you mask.")

        return f"Welcome to {self.name}"
