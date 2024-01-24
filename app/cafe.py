from datetime import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Should be vaccinated")
        expiration_date = visitor["vaccine"]["expiration_date"]
        if datetime.now().date() > expiration_date:
            raise OutdatedVaccineError("Update your vaccine")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Buy a mask")
        return f"Welcome to {self.name}"
