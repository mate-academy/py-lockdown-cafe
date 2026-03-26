from app.errors import NotVaccinatedError
import datetime
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        exp = visitor["vaccine"].get("expiration_date")
        if exp < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is expired")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("No mask")
        return f"Welcome to {self.name}"
