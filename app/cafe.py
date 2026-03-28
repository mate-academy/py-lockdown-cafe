import datetime
from typing import Dict, Any
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def visit_cafe(self, visitor: Dict[str, Any]) -> str:
        """Check if the visitor can enter the cafe."""
        name: str = visitor.get("name", "Visitor")

        if "vaccine" not in visitor:
            raise NotVaccinatedError(name)

        expiration_date: datetime.date = visitor["vaccine"].get(
            "expiration_date"
        )
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(name, expiration_date)

        # Check mask
        wearing_mask: bool = visitor.get("wearing_a_mask", False)
        if not wearing_mask:
            raise NotWearingMaskError(name)

        # Access granted
        return f"Welcome to {self.name}"
