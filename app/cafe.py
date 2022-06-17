from datetime import date

from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        if visitor["vaccine"]['expiration_date'] < date.today():
            raise OutdatedVaccineError
        if visitor["wearing_a_mask"] is True:
            return f"Welcome to {self.name}"
        raise NotWearingMaskError
