import datetime

from .errors import NotWearingMaskError
from .errors import NotVaccinatedError
from .errors import OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor must have a vaccine record.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Descriptive message here")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor must wear a mask.")
        return f"Welcome to {self.name}"
