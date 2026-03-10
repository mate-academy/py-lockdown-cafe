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
            raise NotVaccinatedError("Visitor is not vaccinated.")
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date is None or not isinstance(expiration_date, date):
            raise OutdatedVaccineError("Vaccine is expired")
        if expiration_date < date.today():
            raise OutdatedVaccineError("Vaccine is expired")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor should wear a mask.")
        return f"Welcome to {self.name}"
