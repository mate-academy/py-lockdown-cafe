import datetime
from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor doesn't have a vaccine")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The visitor's vaccine is outdated")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor without a mask")

        return f"Welcome to {self.name}"
