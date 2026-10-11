import datetime
from app.errors import NotVaccinatedError, NotWearingMaskError, OutdatedVaccineError


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Not vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is expired.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Mask is required.")
        return f"Welcome to {self.name}"
