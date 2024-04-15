import datetime

from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> str:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        vaccine_info = visitor.get("vaccine")
        if not vaccine_info:
            raise NotVaccinatedError("Visitor is not vaccinated.")

        expiration_date = vaccine_info.get("expiration_date")
        if expiration_date and expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated.")

        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
