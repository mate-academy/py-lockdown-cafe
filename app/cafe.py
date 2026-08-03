from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> str:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if not visitor.get("vaccine", False):
            raise NotVaccinatedError
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
