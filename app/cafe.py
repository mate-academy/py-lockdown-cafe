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
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You cannot enter without a vaccine")
        vaccine_info = visitor["vaccine"]
        expiration_date = vaccine_info.get("expiration_date")
        if expiration_date is None:
            raise NotVaccinatedError("Vaccine information is incomplete")
        if expiration_date < date.today():
            raise OutdatedVaccineError("The vaccine is expired")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                "You cannot enter without wearing a mask"
            )

        return f"Welcome to {self.name}"
