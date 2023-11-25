from datetime import date
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Not vaccinated.")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("The vaccine be expired.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("All visitors must wear masks.")
        return f"Welcome to {self.name}"
