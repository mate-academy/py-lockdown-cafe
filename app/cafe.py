from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
from datetime import date


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor["vaccine"]:
            raise NotVaccinatedError("You're unvaccinated")
        if visitor["vaccine"]["expiration_date"] < date.today:
            raise OutdatedVaccineError("Your vaccination has expired.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You're not wearing a mask")
        return f"Welcome to {self.name}"