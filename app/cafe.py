from datetime import date
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError

class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor):
        if 'vaccine' not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")
        vaccine = visitor['vaccine']
        expiration_date = vaccine['expiration_date']
        if expiration_date < date.today():
            raise OutdatedVaccineError("Vaccine is expired.")
        if not visitor.get('wearing_a_mask', False):
            raise NotWearingMaskError("Visitor is not wearing a mask.")
        return f"Welcome to {self.name}"
