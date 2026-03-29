from __future__ import annotations
from datetime import datetime
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Not vaccinated")

        vaccine_date = visitor["vaccine"].get("expiration_date")
        if not vaccine_date or vaccine_date < datetime.now().date():
            raise OutdatedVaccineError("Outdated vaccine")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Not wearing a mask")

        return f"Welcome to {self.name}"
