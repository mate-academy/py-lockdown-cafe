from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("All friends should be vaccinated.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The vaccine must not be expired!")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("All visitors must wear masks!")
        return f"Welcome to {self.name}"
