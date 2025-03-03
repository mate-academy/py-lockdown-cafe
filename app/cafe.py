import datetime
from typing import Dict, Any
from app.errors import NotVaccinatedError, OutdatedVaccineError, \
    NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict[str, Any]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "Visitor does not have a vaccine record."
            )
        vaccine = visitor["vaccine"]
        expiration_date = vaccine.get("expiration_date")
        if not isinstance(expiration_date, datetime.date):
            raise OutdatedVaccineError("Invalid expiration date provided.")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is expired.")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask.")
        return f"Welcome to {self.name}"
