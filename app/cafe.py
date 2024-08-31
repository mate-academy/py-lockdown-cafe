import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")

        data_vaccine = visitor["vaccine"]["expiration_date"]
        if data_vaccine < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitot is not wearing a mask.")

        return f"Welcome to {self.name}"
