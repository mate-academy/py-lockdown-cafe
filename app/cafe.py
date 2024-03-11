from datetime import date

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
            raise NotVaccinatedError("All friends should be vaccinated")

        elif visitor["vaccine"].get("expiration_date") < date.today():
            raise OutdatedVaccineError("All friends should have valid vaccine")

        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Friends should buy masks")

        return f"Welcome to {self.name}"

    def __str__(self) -> str:
        return str(self.name)
