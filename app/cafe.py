from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError)


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("visitors aren't vaccinated")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("The vaccine is expired")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor without mask!")
        return f"Welcome to {self.name}"
