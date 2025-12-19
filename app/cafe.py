from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)
import datetime
from typing import Any


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, Any]) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Not vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("outdated vaccine")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("not wearing mask")
        return f"Welcome to {self.name}"
