import datetime
from .errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name = visitor.get("name", "Guest")
        vaccine = visitor.get("vaccine")
        if vaccine is None:
            raise NotVaccinatedError(f"{name} is not vaccinated")

        expiration_date = vaccine.get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"{name}'s vaccine expired on {expiration_date}"
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"{name} is not wearing a mask")

        return f"Welcome to {self.name}"
