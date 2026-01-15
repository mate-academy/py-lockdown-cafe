from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name = visitor["name"]

        if "vaccine" not in visitor:
            raise NotVaccinatedError(name)

        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(name)

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(name)

        return f"Welcome to {self.name}"
