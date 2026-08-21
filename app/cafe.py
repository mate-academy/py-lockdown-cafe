from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> str:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor must be vaccinated")
        if date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("The vaccine is outdated")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("The visitor must wear a mask")
        return f"Welcome to {self.name}"
