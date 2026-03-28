from typing import Any
from datetime import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Any:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        elif visitor["vaccine"]["expiration_date"] < datetime.now().date():
            raise OutdatedVaccineError("Vaccine is expired")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor is not wearing a mask")
        else:
            return f"Welcome to {self.name}"
