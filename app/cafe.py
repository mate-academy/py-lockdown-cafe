import datetime
from app.errors import NotVaccinatedError, OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor should be vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor should wear a mask")
        return f"Welcome to {self.name}"
