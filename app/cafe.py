from __future__ import annotations
from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        vaccine = visitor.get("vaccine", None)
        is_wearing_mask = visitor.get("wearing_a_mask", False)
        if vaccine is None:
            raise NotVaccinatedError(
                "Exception: Visitor not vaccinated"
            )

        exp_date = vaccine["expiration_date"]
        today = date.today()
        if exp_date < today:
            raise OutdatedVaccineError(
                "Exception: Vaccine is outdated"
            )

        if not is_wearing_mask:
            raise NotWearingMaskError(
                "Exception: Visitor is not wearing a mask"
            )

        return f"Welcome to {self.name}"
