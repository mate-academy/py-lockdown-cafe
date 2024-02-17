from __future__ import annotations

import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{self.name} is not vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The vaccine is expired.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("All visitors must wear masks")
        return f"Welcome to {self.name}"
