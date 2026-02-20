import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor has no vaccine info")
        exp = visitor["vaccine"].get("expiration_date")
        if exp is None or exp < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is expired")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing a mask")
        return f"Welcome to {self.name}"
