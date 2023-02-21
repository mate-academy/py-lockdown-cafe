from __future__ import annotations

import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} should be vaccinated")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor['name']} has outdated vaccine"
            )

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor['name']} should buy mask")

        return f"Welcome to {self.name}"
