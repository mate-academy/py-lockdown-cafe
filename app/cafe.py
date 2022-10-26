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
        today = datetime.date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor should have vaccine")
        if visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError("The vaccine has expired")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("The visitor must wear a mask")
        return f"Welcome to {self.name}"
