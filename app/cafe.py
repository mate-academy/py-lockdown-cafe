import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("You have to vaccinate yourself.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("You have to vaccinate again.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You have to wear the mask.")
        return f"Welcome to {self.name}"
