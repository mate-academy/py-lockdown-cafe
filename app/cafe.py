import datetime

from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor must be vaccinated")

        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("The vaccine must not be expired")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor must wear mask")

        return f"Welcome to {self.name}"
