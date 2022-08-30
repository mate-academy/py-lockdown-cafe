import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError
                        )


class Cafe:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor don't have vaccine")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Bad vaccine")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("No mask")
        return f"Welcome to {self.name}"
