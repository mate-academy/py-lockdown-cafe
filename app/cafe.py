import datetime
from app.error import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today:
            raise OutdatedVaccineError
        elif not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError
        else:
            return f"Welcome to {self.name}"
