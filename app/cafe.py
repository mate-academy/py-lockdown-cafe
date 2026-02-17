from __future__ import annotations
import datetime
from typing import Dict, Any
from errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict[str, Any]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError()

        expiration_date: Any = visitor["vaccine"].get("expiration_date")
        if not isinstance(expiration_date, datetime.date):
            raise OutdatedVaccineError()

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError()

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
