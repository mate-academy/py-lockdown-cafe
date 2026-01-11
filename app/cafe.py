import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = datetime.date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        expiration_date = visitor["vaccine"].get("expiration_date")
        if not expiration_date:
            raise ValueError("Vaccine record "
                             "is missing expiration date")
        if expiration_date < today:
            raise OutdatedVaccineError("Vaccine is expired")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask")
        return f"Welcome to {self.name}"
