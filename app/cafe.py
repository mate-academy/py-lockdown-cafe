import datetime
from typing import Any
from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Any:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        vaccine_expiration_date = visitor["vaccine"].get("expiration_date")
        today = datetime.date.today()
        if today > vaccine_expiration_date:
            raise OutdatedVaccineError("Visitor's vaccine is outdated")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("The visitor is not wearing a mask")
        else:
            return f"Welcome to {self.name}"
