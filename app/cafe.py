import datetime

from app import errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise errors.NotVaccinatedError("You must be vaccinated.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise errors.OutdatedVaccineError("Your vaccination has expired.")
        if not visitor["wearing_a_mask"]:
            raise errors.NotWearingMaskError("You should wear a mask.")
        return f"Welcome to {self.name}"
