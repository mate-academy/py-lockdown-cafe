from __future__ import annotations
from datetime import date
from app.errors import NotWearingMaskError
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Vaccine is absent")
        if visitor.get("vaccine").get("expiration_date") < date.today():
            raise OutdatedVaccineError("Vaccine is outdated")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("No mask")
        else:
            return f"Welcome to {self.name}"
