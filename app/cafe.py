from datetime import date
from app.errors import (NotWearingMaskError,
                        OutdatedVaccineError,
                        NotVaccinatedError)


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        if visitor['vaccine']['expiration_date'] < date.today():
            raise OutdatedVaccineError
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError
        return f"Welcome to {self.name}"
