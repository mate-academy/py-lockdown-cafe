from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        vaccine_info = visitor.get("vaccine")
        if not vaccine_info:
            raise NotVaccinatedError(
                "The visitor is not vaccinated"
            )
        if vaccine_info["expiration_date"] < date.today():
            raise OutdatedVaccineError(
                "The visitor's vaccine has expired"
            )
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                "The visitor needs to wear a mask"
            )

        return f"Welcome to {self.name}"
