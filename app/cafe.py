import datetime
from typing import Any


from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, Any]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Outdated vaccine")

        if "wearing_a_mask" not in visitor or not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Not wearing a mask")

        return f"Welcome to {self.name}"
