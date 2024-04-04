from app.errors import *
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitors: dict) -> str:
        if not ("vaccine" in visitors):
            raise NotVaccinatedError("Not Vaccinated")
        if visitors["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Outdated Vaccine")
        if not visitors["wearing_a_mask"]:
            raise NotWearingMaskError("Not Wearing mask")
        return f"Welcome to {self.name}"



