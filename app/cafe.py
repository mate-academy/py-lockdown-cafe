import datetime
from typing import Any, Optional

from app.errors import (
NotVaccinatedError,
OutdatedVaccineError,
NotWearingMaskError
)

class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, Any]) -> Optional[str]:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor is not vaccinated.")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitors vaccination is outdated")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor not wearing a mask")
        return f"Welcome to {self.name}"
