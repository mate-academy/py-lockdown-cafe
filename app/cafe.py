import datetime
from typing import Dict, Any, Optional

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict[str, Any]) -> str:
        name = visitor.get("name", "Unknown")

        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"Visitor {name} is not vaccinated.")

        expiration_date: Optional[datetime.date] = visitor["vaccine"].get(
            "expiration_date"
        )

        if expiration_date is None:
            raise NotVaccinatedError(
                f"Visitor {name}'s "
                f"vaccine record is missing an expiration date."
            )

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(f"Visitor {name}'s vaccine is expired.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"Visitor {name} is not wearing a mask.")

        return f"Welcome to {self.name}"
