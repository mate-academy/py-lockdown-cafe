import datetime

from app.errors import NotVaccinatedError, NotWearingMaskError
from app.errors import OutdatedVaccineError


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated!")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"The {visitor['name']}'s vaccine "
                                       f"has expired!")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("All friends should wear masks")

        return f"Welcome to {self.name}"
