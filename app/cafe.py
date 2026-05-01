from app.errors import OutdatedVaccineError
from app.errors import NotVaccinatedError
from app.errors import NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor must be vaccinated")

        expiration_date = visitor["vaccine"]["expiration_date"]
        today = datetime.date.today()
        if expiration_date < today:
            raise OutdatedVaccineError("Outdated vaccine")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Not wearing mask")

        return f"Welcome to {self.name}"
