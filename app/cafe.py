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
        today = datetime.date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")
        if (
            visitor["vaccine"]["expiration_date"] < today
            or "expiration_date" not in visitor["vaccine"]
        ):
            raise OutdatedVaccineError("OutdatedVaccineError")
        if "wearing_a_mask" not in visitor or not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("NotWearingMaskError")
        return f"Welcome to {self.name}"
