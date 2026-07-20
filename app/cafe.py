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
        vaccine = visitor.get("vaccine")

        if vaccine is None:
            raise NotVaccinatedError(
                f'{visitor.get("name", "Visitor")} is not vaccinated.'
            )

        expiration_date = vaccine.get("expiration_date")

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f'{visitor.get("name", "Visitor")} has an outdated vaccine.'
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f'{visitor.get("name", "Visitor")} is not wearing a mask.'
            )

        return f"Welcome to {self.name}"
