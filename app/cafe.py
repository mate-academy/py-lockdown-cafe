import datetime as dt
from typing import Optional

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Optional[str]:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor has no vaccine key.")
        if visitor["vaccine"]["expiration_date"] < dt.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("No mask on the visitor's face.")

        return f"Welcome to {self.name}"
