from app.errors import OutdatedVaccineError,\
    NotVaccinatedError, NotWearingMaskError

import datetime


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if 'vaccine' not in visitor:
            raise NotVaccinatedError("The visitor is not vaccinated.")
        if visitor['vaccine']['expiration_date']\
                < datetime.date.today():
            raise OutdatedVaccineError("Vaccine has expired.")
        if not visitor['wearing_a_mask']:
            raise NotWearingMaskError("The visitor does not have a mask.")
        return f"Welcome to {self.name}"
