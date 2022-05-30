from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:

    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Some of visitors got no vaccine")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Some of visitors has expired vaccine")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Some of visitors does not have mask")
        return f"Welcome to {self.name}"
