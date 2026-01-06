from errors import (
    VaccineError,
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if 'vaccine' not in visitor:
            raise NotVaccinatedError()

        vaccine = visitor['vaccine']

        if vaccine['expiration_date'] < datetime.date.today():
            raise OutdatedVaccineError()

        if not visitor.get('wearing_a_mask', False):
            raise NotWearingMaskError()

        print(f"Welcome to {self.name}")