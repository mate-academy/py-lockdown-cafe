import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        wearing_a_mask = visitor.get("wearing_a_mask", False)

        if not vaccine:
            raise NotVaccinatedError()

        expiration_date = vaccine.get("expiration_date")

        if not expiration_date or expiration_date < datetime.date.today():
            raise OutdatedVaccineError()

        if not wearing_a_mask:
            raise NotWearingMaskError()

        return f"Welcome to {self.name}"
