from app.errors import OutdatedVaccineError, NotVaccinatedError
from app.errors import NotWearingMaskError
from datetime import date


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor or visitor["vaccine"] is None:
            raise NotVaccinatedError("Visitor is not vaccinated")

        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Vaccine has expired")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
