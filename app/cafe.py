import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        if not vaccine:
            raise NotVaccinatedError("Visitor dont have a vaccine")
        if not (
                vaccine.get("expiration_date")
                >= datetime.date.today()
        ):
            raise OutdatedVaccineError("Vaccine is outdated")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor needs a mask")
        return f"Welcome to {self.name}"
