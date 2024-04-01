from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)
from datetime import date


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError()

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date and expiration_date < date.today():
            raise OutdatedVaccineError()

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError()

        return f"Welcome to {self.name}"
