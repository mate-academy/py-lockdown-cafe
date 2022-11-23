import datetime
from app.errors import (
    OutdatedVaccineError,
    NotWearingMaskError,
    NotVaccinatedError
)


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The friend is not vaccinated")
        if visitor["vaccine"]["expiration_date"]\
                < datetime.date.today():
            raise OutdatedVaccineError("The vaccine is outdated")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("The friend is not wearing a mask")
        return f"Welcome to {self.name}"
