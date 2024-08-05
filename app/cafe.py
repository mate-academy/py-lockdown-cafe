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

        vaccine_info = visitor["vaccine"]
        if vaccine_info["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
