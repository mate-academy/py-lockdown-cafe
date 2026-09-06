from app.errors import NotVaccinatedError, OutdatedVaccineError
from app.errors import NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Not vaccinated")
        expire_date = visitor["vaccine"]["expiration_date"]
        if expire_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine expired")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("No mask")

        return f"Welcome to {self.name}"
