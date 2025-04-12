# app/cafe.py
import datetime
from .errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        visitor_name = visitor.get("name", "Unknown")
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"Visitor '{visitor_name}' is not vaccinated."
            )
        vaccine = visitor["vaccine"]
        expiration_date = vaccine.get("expiration_date")
        if expiration_date is None:
            raise NotVaccinatedError(
                f"Visitor '{visitor_name}' has no valid vaccine info."
            )
        today = datetime.date.today()
        if expiration_date < today:
            message = (
                f"Visitor '{visitor_name}' vaccine expired on "
                f"{expiration_date}."
            )
            raise OutdatedVaccineError(message)
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"Visitor '{visitor_name}' is not wearing a mask."
            )
        return f"Welcome to {self.name}"
