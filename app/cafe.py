import datetime
from app.errors import NotWearingMaskError, NotVaccinatedError, \
    OutdatedVaccineError


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"Vaccination is "
                                     f"required to enter {self.name}.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Unfortunately, "
                                       "your vaccination is outdated.")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Please, put on a mask.")
        return f"Welcome to {self.name}"
