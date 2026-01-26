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
        self.name: str = name

    def visit_cafe(self, visitor: Dict[str, Any]) -> str:
        visitor_name: str = visitor.get("name", "Unknown visitor")

        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor_name} is not vaccinated")

        vaccine_info = visitor["vaccine"]
        expiration_date = vaccine_info.get("expiration_date")

        if not isinstance(expiration_date, datetime.date):
            raise OutdatedVaccineError(
                f"Invalid vaccine data for {visitor_name}"
            )

        today: datetime.date = datetime.date.today()
        if expiration_date < today:
            raise OutdatedVaccineError(
                f"Vaccine for {visitor_name} is outdated"
            )

        wearing_a_mask: bool = bool(visitor.get("wearing_a_mask", False))
        if not wearing_a_mask:
            raise NotWearingMaskError(f"{visitor_name} is not wearing a mask")

        return f"Welcome to {self.name}"
