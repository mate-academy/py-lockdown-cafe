from __future__ import annotations
import datetime
from typing import Any, Dict

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict[str, Any]) -> str:
        name = str(visitor.get("name", "Visitor"))

        # Vaccine presence
        vaccine = visitor.get("vaccine")
        if not isinstance(vaccine, dict):
            raise NotVaccinatedError(
                f"{name} has no vaccine record access denied to {self.name}"
            )

        if "expiration_date" not in vaccine:
            raise NotVaccinatedError(
                f"{name} has no expiration date access denied to {self.name}"
            )

        expiration_date = vaccine["expiration_date"]
        today = datetime.date.today()
        if expiration_date < today:
            raise OutdatedVaccineError(
                f"{name}'s vaccine expired on {expiration_date}"
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                f"{name} must wear a mask to enter {self.name}"
            )

        return f"Welcome to {self.name}"
#
