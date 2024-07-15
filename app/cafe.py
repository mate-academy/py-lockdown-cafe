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
            raise NotVaccinatedError(
                "Sorry, you are not vaccinated."
            )
        if visitor.get("vaccine").get("expiration_date") < date.today():
            raise OutdatedVaccineError(
                "Sorry, you vaccination is expired."
            )
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                "Please buy a mask."
            )
        return f"Welcome to {self.name}"
