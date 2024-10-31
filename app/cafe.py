from datetime import datetime
from typing import Dict

from app.errors import (
    OutdatedVaccineError,
    NotWearingMaskError,
    NotVaccinatedError
)


class Cafe:
    """General class representing cafe."""
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict) -> str:
        """Check if visitor can visit a cafe."""
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated!")

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.now().date():
            raise OutdatedVaccineError("Visitor has outdated vaccine!")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing a mask!")

        return f"Welcome to {self.name}"
