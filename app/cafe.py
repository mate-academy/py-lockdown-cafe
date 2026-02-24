from app.errors import NotVaccinatedError, OutdatedVaccineError
from app.errors import NotWearingMaskError
import datetime
from typing import Dict, Any


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict[str, Any]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date is None:
            raise OutdatedVaccineError("Vaccine expiration date is missing.")

        if isinstance(expiration_date, str):
            try:
                expiration_date = datetime.datetime.strptime(
                    expiration_date, "%Y-%m-%d").date()
            except ValueError:
                raise OutdatedVaccineError(
                    "Invalid date format for vaccine expiration date.")

        if not isinstance(expiration_date, datetime.date):
            raise OutdatedVaccineError(
                "Expiration date must be a datetime.date object.")

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
