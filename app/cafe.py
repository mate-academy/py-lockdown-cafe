import datetime
from typing import Any
from app.errors import NotWearingMaskError, OutdatedVaccineError, NotVaccinatedError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Any:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("All friends should be vaccinated")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("All friends should be vaccinated")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("All friends should be vaccinated")
        return f"Welcome to {self.name}"
