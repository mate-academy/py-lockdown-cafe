import datetime
from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"Sorry, {visitor['name']} "
                                     f"doesn't have vaccine")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"Sorry, {visitor['name']}'s "
                                       f"vaccine is expired")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"Sorry, {visitor['name']} "
                                      f"doesn't have mask")

        return f"Welcome to {self.name}"
