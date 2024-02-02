import datetime
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor):
        if 'vaccine' not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")
        if visitor['vaccine']['expiration_date'] < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated.")
        if not visitor.get('wearing_a_mask', False):
            raise NotWearingMaskError("Visitor is not wearing a mask.")
        return f"Welcome to {self.name}"
