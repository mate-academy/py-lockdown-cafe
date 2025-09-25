import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(visitor["name"])
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(visitor["name"])
        elif not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(visitor["name"])
        else:
            return f"Welcome to {self.name}"
