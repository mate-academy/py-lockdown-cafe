from datetime import date

from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if not visitor.get("vaccine"):
            raise NotVaccinatedError
        if visitor["vaccine"].get("expiration_date") < date.today():
            raise OutdatedVaccineError
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
