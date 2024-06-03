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
        name = visitor["name"]
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{name} should be vaccinated")

        if date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError(f"{name} should be vaccinated")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(f"Visitor {name} must wear masks")

        return f"Welcome to {self.name}"
