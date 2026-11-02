from typing import Any
import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, Any]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Not vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Outdated vaccine")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Not wearing mask")
        return f"Welcome to {self.name}"
