import datetime

from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if not visitor.get("vaccine", 0):
            raise NotVaccinatedError("The visitor must be vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The vaccine mustn't be expired")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("The visitor must wear a mask")
        return f"Welcome to {self.name}"
