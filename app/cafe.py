from __future__ import annotations
from datetime import date
from app.errors import NotWearingMaskError, NotVaccinatedError, OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date is not None and expiration_date < date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")

        if not visitor.get("wearing_a_mask", True):
            raise NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"
