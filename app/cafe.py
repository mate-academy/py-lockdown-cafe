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
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("Visitor is not vaccinated.")
        elif visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated.")
        elif visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("Visitor doesn't wear mask.")
        return f"Welcome to {self.name}"
