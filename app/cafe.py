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
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if not isinstance(expiration_date, datetime.date):
            raise OutdatedVaccineError(
                "Visitor's vaccine expiration date is invalid"
            )
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
