import datetime
from typing import Any
from app.errors import NotWearingMaskError
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Any:

        if not visitor.get("vaccine", False):
            raise NotVaccinatedError("Visitor has no vaccine")

        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine expired")

        elif not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Wearing a mask is required")

        else:
            return f"Welcome to {self.name}"
