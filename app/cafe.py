import datetime
from app.errors import \
    NotWearingMaskError, \
    OutdatedVaccineError, \
    NotVaccinatedError


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All friends should be vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Friends should buy 2 masks")
        return f"Welcome to {self.name}"
