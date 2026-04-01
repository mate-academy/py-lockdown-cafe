import datetime

from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        # Check if visitor has vaccine key at all
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"Visitor {visitor['name']} is not vaccinated."
            )

        # Check if vaccine is expired — expiration date must be today or later
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f"Visitor {visitor['name']} has an outdated vaccine."
            )

        # Check if visitor is wearing a mask
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f"Visitor {visitor['name']} is not wearing a mask."
            )

        return f"Welcome to {self.name}"
