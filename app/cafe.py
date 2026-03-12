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
        if not visitor.get("vaccine", 0):
            raise NotVaccinatedError("Not Vaccinated")
        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("Outadated Vaccine")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Not Wearing Mask")
        return f"Welcome to {self.name}"
