from app.errors import NotVaccinatedError,\
    OutdatedVaccineError,\
    NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor):
        if "vaccine" not in visitor:
            raise NotVaccinatedError

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
1