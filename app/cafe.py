import datetime
from app.errors import NotVaccinatedError, \
    NotWearingMaskError,\
    OutdatedVaccineError


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if 'vaccine' not in visitor:
            raise NotVaccinatedError
        if visitor["vaccine"]['expiration_date'] < datetime.date.today():
            raise OutdatedVaccineError
        if visitor['wearing_a_mask'] is False:
            raise NotWearingMaskError
        return f"Welcome to {self.name}"
