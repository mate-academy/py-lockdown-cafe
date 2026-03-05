from datetime import date
from typing import Any

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, str | bool | dict[str, Any]]) -> str:

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Not vaccinated visitor cannot enter the cafe.")

        expiration = visitor["vaccine"]["expiration_date"]
        if expiration < date.today():
            raise OutdatedVaccineError(
                "Vaccine has expired. Visitor cannot enter the cafe."
            )

        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError(
                "Visitor should be wearing a mask to enter the cafe."
            )

        return f"Welcome to {self.name}"
