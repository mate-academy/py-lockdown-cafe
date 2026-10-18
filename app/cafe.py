import datetime
from typing import Any

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, Any]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "A valid vaccine certificate is required."
            )

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("The visitor's vaccine has expired.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("The visitor must wear a mask.")

        return f"Welcome to {self.name}"
