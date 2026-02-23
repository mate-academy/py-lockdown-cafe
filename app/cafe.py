import datetime

from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor is not vaccinated.")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine has expired.")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
