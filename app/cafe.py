from datetime import date

from app.errors import (
    NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str]) -> str | Exception:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor is not vaccinated.")
        if visitor["vaccine"].get("expiration_date") < date.today():
            raise OutdatedVaccineError("Vaccine is expired")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
