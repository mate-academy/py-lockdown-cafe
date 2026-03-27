from datetime import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor is not vaccinated")

        vaccine_expiry = visitor["vaccine"].get("expiration_date")
        if datetime.now().date() > vaccine_expiry:
            raise OutdatedVaccineError("Your vaccine is outdated")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("You should wear a mask")

        return f"Welcome to {self.name}"
