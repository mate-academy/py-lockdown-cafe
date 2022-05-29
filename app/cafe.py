from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)

today = date.today()


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError
        if visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError
        return f"Welcome to {self.name}"
