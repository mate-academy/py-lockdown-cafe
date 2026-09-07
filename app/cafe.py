import datetime
from typing import Any

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, Any]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")

        expiration_date: datetime.date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine has expired.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
