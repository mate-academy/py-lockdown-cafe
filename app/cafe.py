import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine", False):
            raise NotVaccinatedError(
                "Visitor is not vaccinated.")
        if not isinstance(
                visitor["vaccine"]["expiration_date"], datetime.date):
            raise ValueError("Invalid date format. Expected datetime.date.")
        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError(
                "Out dated Vaccine Error.")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                "NotWearingMaskError.")
        return f"Welcome to {self.name}"
