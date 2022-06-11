from datetime import date

from app.errors import NotVaccinatedError,\
    OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You don't have vaccine")

        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Your vaccine is obsolete!")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You don't have a mask!")

        return f"Welcome to {self.name}"
