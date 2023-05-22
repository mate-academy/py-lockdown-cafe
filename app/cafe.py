import datetime
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Vaccine information is missing.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated.")
        if (
                "wearing_a_mask" not in visitor or visitor["wearing_a_mask"]
        ) is False:
            raise NotWearingMaskError("Visitor without a mask")
        return f"Welcome to {self.name}"
