import datetime
from app.errors import OutdatedVaccineError,\
    NotWearingMaskError, NotVaccinatedError


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        if "expiration_date" not in visitor["vaccine"] or \
                visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError
        return f"Welcome to {self.name}"
