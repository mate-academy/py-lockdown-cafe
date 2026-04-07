import datetime

from app.errors import (
    OutdatedVaccineError,
    NotWearingMaskError,
    NotVaccinatedError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} don't have vaccine!")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor['name']}'s vaccine expired!")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{visitor['name']} without a mask!")
        return f"Welcome to {self.name}"
