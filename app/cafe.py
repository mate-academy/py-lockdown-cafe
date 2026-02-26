import datetime
from app.errors import (
    NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"Visitor {visitor["name"]} is not vaccinated!")

        vaccine_expiration = visitor["vaccine"]["expiration_date"]
        if vaccine_expiration < datetime.date.today():
            raise OutdatedVaccineError(
                f"Visitor {visitor["name"]}'s vaccine has expired!")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"Visitor {visitor["name"]} is not wearing a mask!")

        return f"Welcome to {self.name}"
