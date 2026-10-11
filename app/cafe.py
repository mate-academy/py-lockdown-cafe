
import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)
from typing import Any


class Cafe:
    def __init__(self, name: str) -> Any:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "Visitor is not vaccinated"
            )

        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError(
                f"{visitor['name']} has an outdated vaccine"
            )

        if ("wearing_a_mask" not in visitor
                or visitor["wearing_a_mask"] is False):
            raise NotWearingMaskError(
                f"{visitor['name']} is not wearing a mask"
            )

        return f"Welcome to {self.name}"
