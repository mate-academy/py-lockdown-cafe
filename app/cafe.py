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
        name = visitor.get("name", "Visitor")

        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{name} is not vaccinated")

        vaccine = visitor[
            "vaccine"
        ]
        expiration_date = vaccine.get("expiration_date")

        if expiration_date is None:
            raise OutdatedVaccineError(
                f"{name} has no expiration date for the vaccine"
            )

        if not isinstance(expiration_date, datetime.date):
            raise TypeError(f"Invalid expiration_date type for {name}")

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(f"{name} has an outdated vaccine")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"{name} is not wearing a mask")
        return f"Welcome to {self.name}"
