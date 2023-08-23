from datetime import date
from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        vaccine = visitor.get("vaccine")
        if not vaccine:
            raise NotVaccinatedError("Visitor does't have vaccine.")
        if date.today() > vaccine.get("expiration_date"):
            raise OutdatedVaccineError("Vaccine's expiration date has passed.")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visito doesn't have a mask.")
        return f"Welcome to {self.name}"
