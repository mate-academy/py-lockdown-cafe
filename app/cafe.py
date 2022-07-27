from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor must have a valid vaccine")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine must be valid")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor must wear facemask")
        return f"Welcome to {self.name}"
