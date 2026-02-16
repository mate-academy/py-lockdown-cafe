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
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "Visitor does not have a vaccination record."
            )

        vaccine_info = visitor["vaccine"]
        expiration_date = vaccine_info.get("expiration_date")

        if not isinstance(expiration_date, datetime.date):
            raise OutdatedVaccineError(
                f"Vaccine expiration date must be a valid date,"
                f" got {type(expiration_date).__name__}."
            )

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"Visitor's vaccine expired on {expiration_date}."
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                "Visitor is not wearing a mask. Entry denied."
            )

        return f"Welcome to {self.name}"
