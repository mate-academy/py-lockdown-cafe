import datetime

from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All friends should be vaccinated")
        # else:
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Your vaccine is expired")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
