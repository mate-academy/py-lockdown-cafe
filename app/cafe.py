from __future__ import annotations

import datetime

from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(f"{self.name} will die from corona!")
        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError(
                f"{self.name}'s vaccine has already expired."
            )
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Put on your mask please!")
        return f"Welcome to {self.name}"
