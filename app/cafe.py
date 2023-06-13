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
            raise NotVaccinatedError("You should be vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.today().date():
            raise OutdatedVaccineError("Your vaccine should be valid")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("You should wear a mask")
        return f"Welcome to {self.name}"
