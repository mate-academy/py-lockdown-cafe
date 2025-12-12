from datetime import date
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError
from app.errors import NotVaccinatedError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine", False):
            raise NotVaccinatedError("Visitor must be vaccinated")
        if visitor.get("vaccine").get("expiration_date") < date.today():
            raise OutdatedVaccineError("Visitors vaccine is outdated")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor has not a mask")
        return f"Welcome to {self.name}"
