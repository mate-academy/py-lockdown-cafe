import datetime
from app.errors import (
    NotWearingMaskError,
    OutdatedVaccineError,
    NotVaccinatedError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("All friends should be vaccinated")
        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("All friends should be vaccinated")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("All visitors must wear a mask")
        return f"Welcome to {self.name}"
