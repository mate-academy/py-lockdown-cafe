import datetime

from app.errors import NotVaccinatedError,\
    OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):

        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor is not vaccinated.")
        if "expiration_date" not in visitor['vaccine']:
            raise OutdatedVaccineError
        elif visitor['vaccine']['expiration_date'] < datetime.date.today():
            raise OutdatedVaccineError
        if 'wearing_a_mask' not in visitor:
            raise NotWearingMaskError
        elif not visitor['wearing_a_mask']:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
