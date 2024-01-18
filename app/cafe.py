from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | Exception:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor should be vaccinated.")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("The vaccine must not be expired.")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("All visitors must wear masks.")
        return f"Welcome to {self.name}"
