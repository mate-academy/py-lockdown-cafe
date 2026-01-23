import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Person not vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccines out of date")
        if "wearing_a_mask" not in visitor:
            raise NotWearingMaskError("Not wearing Mask not allowwed")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Not wearing Mask not allowed")
        return f"Welcome to {self.name}"
