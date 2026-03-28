import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        self.visitor = visitor
        try:
            vaccine = visitor["vaccine"]
        except KeyError:
            raise NotVaccinatedError("Not Vaccinated")

        try:
            expiration_date = vaccine["expiration_date"]
            if isinstance(expiration_date, str):
                expiration_date = datetime.date.fromisoformat(expiration_date)
        except KeyError:
            raise OutdatedVaccineError("Outdated Vaccine")

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Outdated Vaccine")

        try:
            if not visitor["wearing_a_mask"]:
                raise NotWearingMaskError("Not wearing a mask")
        except KeyError:
            raise NotWearingMaskError("Not wearing a mask")

        return f"Welcome to {self.name}"
