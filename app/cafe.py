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
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor is not vaccinated.")
        if visitor.get("vaccine", {}).get("expiration_date") < date.today():
            raise OutdatedVaccineError("The vaccine is outdated.")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("All visitors must wear masks.")
        return f"Welcome to {self.name}"
