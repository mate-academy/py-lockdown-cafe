from datetime import date

from app.errors import NotVaccinatedError,\
    OutdatedVaccineError, NotWearingMaskError


class Cafe:

    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        today = date.today()
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("visitor don't have vaccine")
        if visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError("visitor has outdated vaccine")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("visitor must wear a mask")
        return f"Welcome to {self.name}"
