from datetime import date
from app.errors import (
    NotVaccinatedError, NotWearingMaskError, OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("All friends should be vaccinated")

        if visitor.get("vaccine").get("expiration_date") < date.today():
            raise OutdatedVaccineError("Outdated vaccine")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("All visitors must wearing a mask!")

        return f"Welcome to {self.name}"
