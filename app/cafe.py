from datetime import date
from .errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        if not isinstance(vaccine, dict) or "expiration_date" not in vaccine:
            raise NotVaccinatedError("Invalid or missing vaccine information")
        elif vaccine["expiration_date"] < date.today():
            raise OutdatedVaccineError()
        elif not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError()
        else:
            return f"Welcome to {self.name}"

