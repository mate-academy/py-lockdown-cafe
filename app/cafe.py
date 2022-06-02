import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("visitors aren't vaccinated")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The vaccine is expired")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor without mask!")
        else:
            return f"Welcome to {self.name}"
