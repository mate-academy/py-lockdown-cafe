from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)
from datetime import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated")
        elif datetime.now().date() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError(f"{visitor['name']}'s vaccine outdated")
        elif "wearing_a_mask" not in visitor or not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor['name']} should wear a mask")
        else:
            return f"Welcome to {self.name}"
