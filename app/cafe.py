from datetime import date
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
        name = visitor.get("name", "<unknown>")
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{name} is not vaccinated"
            )
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(
                f"{name}'s vaccine is outdated"
            )
        if visitor["wearing_a_mask"] is not True:
            raise NotWearingMaskError(
                f"{name} is not wearing a mask"
            )
        return f"Welcome to {self.name}"
