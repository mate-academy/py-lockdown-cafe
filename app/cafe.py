from __future__ import annotations
from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("All friends should be vaccinated")
        if not self.is_valid_vaccine_date(
                visitor["vaccine"]["expiration_date"]
        ):
            raise OutdatedVaccineError("All friends should be vaccinated")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("You should wear a mask")
        return f"Welcome to {self.name}"

    @staticmethod
    def is_valid_vaccine_date(vaccine_date: date) -> bool:
        curr_date = date.today()
        return curr_date <= vaccine_date
