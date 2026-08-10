import datetime

from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name = visitor.get("name")

        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{name} is not vaccinated.")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date and expiration_date < datetime.date.today():
            raise OutdatedVaccineError(f"{name}'s vaccine is outdated.")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{name} is not wearing a mask.")

        return f"Welcome to {self.name}"
