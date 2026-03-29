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

    def visit_cafe(self, visitor: dict) -> Any:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitors vaccine is expired.")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor is not wearing a mask.")
        else:
            return f"Welcome to {self.name}"
