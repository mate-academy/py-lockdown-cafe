from __future__ import annotations
import datetime
from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Expired vaccine")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor must wear a mask")
        return f"Welcome to {self.name}"
