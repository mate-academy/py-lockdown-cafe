import datetime

from app.errors import (
    OutdatedVaccineError,
    NotVaccinatedError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError
        elif visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError
        return f"Welcome to {self.name}"
