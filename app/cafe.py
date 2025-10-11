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
            raise NotVaccinatedError("Not vaccinated")
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date is None or expiration_date < date.today():
            raise OutdatedVaccineError("Vaccine is outdated or missing")
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Not wearing mask")
        return f"Welcome to {self.name}"
