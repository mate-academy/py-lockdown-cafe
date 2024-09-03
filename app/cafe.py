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
            raise NotVaccinatedError("Visitor does not have a vaccine record.")

        expiration_date = vaccine.get("expiration_date")

        if expiration_date is None or expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                "Vaccine is either missing or has expired."
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
