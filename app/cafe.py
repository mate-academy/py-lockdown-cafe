from app.errors import NotWearingMaskError, NotVaccinatedError, OutdatedVaccineError
from datetime import date


class Cafe:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    def visit_cafe(self, visitor: dict):
        if 'vaccine' not in visitor:
            raise NotVaccinatedError
        if visitor['vaccine']['expiration_date'] < date.today():
            raise OutdatedVaccineError
        if not visitor['wearing_a_mask']:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
