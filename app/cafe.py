from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All visitors must be vaccinated!")
        if visitor["vaccine"].get("expiration_date") < date.today():
            raise OutdatedVaccineError("Sorry, your vaccine is expired.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("All visitor must wear a mask!")
        return f"Welcome to {self.name}"
