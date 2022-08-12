import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("You should be vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("You have to get the vaccine again")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Put on the mask, please!")
        return f"Welcome to {self.name}"
