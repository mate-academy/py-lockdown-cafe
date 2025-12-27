from app.errors import (
    NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Not vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Outdated vaccine")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Not wearing a mask")
        return f"Welcome to {self.name}"
