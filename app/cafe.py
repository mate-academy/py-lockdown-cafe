from datetime import date
from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        if visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError
        if "wearing_a_mask" in visitor:
            if not visitor["wearing_a_mask"]:
                raise NotWearingMaskError
        return f"Welcome to {self.name}"
