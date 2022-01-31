import datetime
from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, \
    NotWearingMaskError


class Cafe:

    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} should have vaccine")
        if "vaccine" in visitor and visitor["vaccine"]["expiration_date"] \
                < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor['name']}"
                                       f" has an expired vaccine")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(f"{visitor['name']}"
                                      f" please put on a mask")
        return f"Welcome to {self.name}"
