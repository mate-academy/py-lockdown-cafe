import datetime
from app.errors import NotWearingMaskError, \
    OutdatedVaccineError,\
    NotVaccinatedError


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You must be a vaccinated")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("You must update you vaccine")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("You must be wearing a mask")
        else:
            return f"Welcome to {self.name}"
