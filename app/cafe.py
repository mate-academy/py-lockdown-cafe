from app.errors import NotVaccinatedError
from app.errors import NotWearingMaskError
from app.errors import OutdatedVaccineError

from datetime import date


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        # vaccination check
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        date_of_end = visitor["vaccine"]["expiration_date"]

        if date_of_end < date.today():
            raise OutdatedVaccineError

        # mask check
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError

        # everything is okay
        return f"Welcome to {self.name}"
