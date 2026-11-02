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
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor hasn't vaccine.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine has expired.")
        if (
            "wearing_a_mask" in visitor
            and visitor["wearing_a_mask"] is False
        ):
            raise NotWearingMaskError("Visitor isn't wearing a mask.")

        return f"Welcome to {self.name}"
