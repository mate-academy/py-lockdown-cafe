from datetime import date
from typing import Any

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, Any]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Vaccine is outdated")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor must wear a mask")

        return f"Welcome to {self.name}"
