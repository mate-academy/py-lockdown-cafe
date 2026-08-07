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
            raise NotVaccinatedError("Visitor does not have a vaccine record.")

        vaccine = visitor["vaccine"]
        expiration_date = vaccine.get("expiration_date")
        if expiration_date is None or expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is expired.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
