import datetime

from app.errors import NotVaccinatedError, OutdatedVaccineError,\
    NotWearingMaskError


class Cafe:

    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor):

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f"Please, {visitor['name']} put on a mask")
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"Sorry, {visitor['name']} entrance only for vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f"Sorry, {visitor['name']} your vaccine is out of date")

        return f"Welcome to {self.name}"
