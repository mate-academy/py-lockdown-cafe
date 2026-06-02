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
        date_today = date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated.")
        if date_today > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError(
                f"{visitor['name']} "
                f"has an expired vaccine."
            )
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{visitor['name']} "
                f"is not wearing a mask.")
        return f"Welcome to {self.name}"
