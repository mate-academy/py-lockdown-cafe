from datetime import date
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name = visitor["name"]

        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{name} does not have the vaccine")

        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(f"{name}`s vaccine is out of date")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{name} does not wear a mask")

        return f"Welcome to {self.name}"
