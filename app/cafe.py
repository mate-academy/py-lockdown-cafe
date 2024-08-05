from datetime import date

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine") or visitor.get("vaccine") is None:
            raise NotVaccinatedError("The visitor must have a vaccine")
        if (visitor.get("vaccine").get("expiration_date") < date.today()
                or visitor.get("vaccine").get("expiration_date") is None):
            raise OutdatedVaccineError("The vaccine must not be expired")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("The visitor must wear mask")

        return f"Welcome to {self.name}"
