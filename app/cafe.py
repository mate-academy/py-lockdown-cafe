import datetime
from app.errors import NotWearingMaskError
from app.errors import NotVaccinatedError, OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor not vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine of visitor is outdated")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor not wearing mask")
        else:
            return f"Welcome to {self.name}"
