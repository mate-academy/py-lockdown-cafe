from datetime import datetime

from app.errors import (
    NotWearingMaskError,
    OutdatedVaccineError,
    NotVaccinatedError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_date = visitor["vaccine"].get("expiration_date")

        if datetime.now().date() > expiration_date:
            raise OutdatedVaccineError("Your vaccine is outdated")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("You should wear a mask")

        return f"Welcome to {self.name}"
