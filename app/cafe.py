from datetime import date
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError, NotWearingMaskError


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor has no vaccine")
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Outdated vaccine")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor is not wearing a mask")
        return f"Welcome to {self.name}"
