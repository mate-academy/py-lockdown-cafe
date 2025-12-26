from datetime import date
from app import errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise errors.NotVaccinatedError("Visitor is not vaccinated.")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise errors.OutdatedVaccineError("Vaccine is outdated.")
        if visitor["wearing_a_mask"] is False:
            raise errors.NotWearingMaskError("Visitor is not wearing a mask.")
        return f"Welcome to {self.name}"
