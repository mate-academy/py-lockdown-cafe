from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError
from datetime import date


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Someone does not have a vaccine")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Someone's vaccine is expired")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Someone does not wear a mask")
        else:
            return f"Welcome to {self.name}"
