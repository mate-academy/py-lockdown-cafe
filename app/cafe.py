from __future__ import annotations
from datetime import date
from app.errors import (
    NotWearingMaskError, NotVaccinatedError, OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor['name']} not vaccinated yet"
            )

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date is not None and expiration_date < date.today():
            raise OutdatedVaccineError(
                f"{visitor['name']} have outdated vaccine"
            )

        if not visitor.get("wearing_a_mask", True):
            raise NotWearingMaskError(
                f"{visitor['name']} not wearing mask"
            )

        return f"Welcome to {self.name}"
