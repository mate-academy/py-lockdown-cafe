import datetime
from typing import Dict, Any

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict[str, Any]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor.get('name')} is not vaccinated."
            )

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor.get('name')} has an outdated vaccine."
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                f"{visitor.get('name')} is not wearing a mask."
            )

        return f"Welcome to {self.name}"
