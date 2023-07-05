import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor should be vaccined")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor vaccination was expired")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Please wear mask")
        return f"Welcome to {self.name}"
