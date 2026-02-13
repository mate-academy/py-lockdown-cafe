import datetime
from typing import Any

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, Any]) -> str:
        name = visitor.get("name", "unknown")

        vaccine = visitor.get("vaccine")
        if not isinstance(vaccine, dict):
            raise NotVaccinatedError(f"Visitor {name} is not vaccinated")

        expiration_date = vaccine.get("expiration_date")
        if not isinstance(expiration_date, datetime.date):
            raise OutdatedVaccineError(
                f"Missing or invalid expiration_date for visitor {name}"
            )

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"Visitor {name}'s vaccine is expired \
                (expired on {expiration_date})"
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"Visitor {name} is not wearing a mask")

        return f"Welcome to {self.name}"
