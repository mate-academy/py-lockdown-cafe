import datetime
from typing import Any

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, Any]) -> str:
        today = datetime.date.today()

        if "vaccine" not in visitor:
            raise NotVaccinatedError("To enter, you have to be vaccinated!")

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < today:
            raise OutdatedVaccineError(
                "Your vaccine is outdated! Please renew it."
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Please, wear a mask before entering!")

        return f"Welcome to {self.name}"
