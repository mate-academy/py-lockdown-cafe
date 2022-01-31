import datetime

from app.errors import NotVaccinatedError, OutdatedVaccineError,\
    NotWearingMaskError


class Cafe:

    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor):

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError

        return f"Welcome to {self.name}"
