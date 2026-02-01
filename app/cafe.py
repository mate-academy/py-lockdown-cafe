import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Not vaccinated")
        elif (datetime.date.today()
              > visitor["vaccine"]["expiration_date"]):
            raise OutdatedVaccineError("Outdated Vaccine")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Not wearing Mask")
        return f"Welcome to {self.name}"
