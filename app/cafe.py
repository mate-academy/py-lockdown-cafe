import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError)


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor):
        try:
            if "vaccine" not in visitor:
                raise NotVaccinatedError

            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError

            if visitor["wearing_a_mask"] is False:
                raise NotWearingMaskError
        except Exception as error:
            raise error
        else:
            return f"Welcome to {self.name}"
