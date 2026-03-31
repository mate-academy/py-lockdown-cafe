import datetime

from app.errors import (
    OutdatedVaccineError,
    NotWearingMaskError,
    NotVaccinatedError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine_info = visitor.get("vaccine")
        if not vaccine_info:
            raise NotVaccinatedError("Visitor is not vaccinated.")

        vaccine_exp = vaccine_info.get("expiration_date")
        if vaccine_exp < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated.")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing mask.")

        return f"Welcome to {self.name}"
