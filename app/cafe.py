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
            raise NotVaccinatedError("Not Vaccinated")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Outdated Vaccine")
        elif not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Not Wearing Mask")
        return f"Welcome to {self.name}"
