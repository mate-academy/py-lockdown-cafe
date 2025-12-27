# cafe.py
from __future__ import annotations

import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        exp = visitor["vaccine"].get("expiration_date")
        today = datetime.date.today()
        if not isinstance(exp, datetime.date) or exp < today:
            raise OutdatedVaccineError(exp)

        has_mask = bool(visitor.get("wearing_a_mask", False))
        if not has_mask:
            raise NotWearingMaskError("Mask is required")

        return f"Welcome to {self.name}"
