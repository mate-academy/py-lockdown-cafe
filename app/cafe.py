from __future__ import annotations

import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor['name']} must get vaccinated to visit {self.name}"
            )
        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError(
                f"{visitor['name']}'s vaccination is expired"
            )
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f"{visitor['name']} is not wearing a mask"
            )
        return f"Welcome to {self.name}"
