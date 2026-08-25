import datetime
from typing import Any

from errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, Any]) -> str:
        vaccine_info = visitor.get("vaccine")

        # Перевірка наявності та коректності структури vaccine
        if not isinstance(vaccine_info, dict) or "expiration_date" not in vaccine_info:
            raise NotVaccinatedError(
                f"Visitor {visitor.get('name', 'Unknown')} is not vaccinated."
            )

        expiration_date = vaccine_info["expiration_date"]

        # Захист від некоректного типу дати
        if not isinstance(expiration_date, datetime.date):
            raise OutdatedVaccineError(
                f"Vaccine date for {visitor.get('name', 'Unknown')} is invalid."
            )

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"Vaccine of {visitor.get('name', 'Unknown')} is outdated."
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"Visitor {visitor.get('name', 'Unknown')} is not wearing a mask."
            )

        return f"Welcome to {self.name}"