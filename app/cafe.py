import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        if not vaccine:
            raise NotVaccinatedError(
                "Visitor '{visitor.get(name)}' has no vaccination"
            )

        expiration_date = vaccine.get("expiration_date")
        if not expiration_date:
            raise NotVaccinatedError(
                "Visitor '{visitor.get(name)}' has no "
                "expiration date in vaccine data"
            )

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                "Visitor '{visitor.get(name)}' has an expired vaccine"
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                "Visitor '{visitor.get(name)}' is not wearing a mask"
            )

        return f"Welcome to {self.name}"
