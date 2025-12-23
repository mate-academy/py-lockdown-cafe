import datetime
from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor must be a vaccine")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine must have a valid vaccine")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor must have mask")
        return f"Welcome to {self.name}"
