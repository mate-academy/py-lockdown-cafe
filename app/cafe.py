from __future__ import annotations

from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
from datetime import date


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name


    def visit_cafe(self, visitor: dict):
        expiration_date = visitor["vaccine"].get("expiration_date")
        if not isinstance(expiration_date, date):
            raise TypeError("expiration_date must be a datetime.date object")
        if not "vaccine" in visitor.keys():
            raise NotVaccinatedError()
        if expiration_date < date.today():
            raise OutdatedVaccineError()
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError()
        return f"Welcome to {self.name}"
