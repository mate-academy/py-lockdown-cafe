from datetime import date
from typing import Dict

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")

        expiration_date = visitor["vaccine"]["expiration_date"]
        today = date.today()

        if expiration_date < today:
            raise OutdatedVaccineError("The vaccine is outdated.")

        wearing_a_mask = visitor["wearing_a_mask"]

        if not wearing_a_mask:
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
