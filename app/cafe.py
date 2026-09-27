from datetime import date
from app.errors import (
    NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Key vaccine not in visitor")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(
                """Expired vaccine | {visitor["vaccine"]["expiration_date"]}"""
            )
        if (
            "wearing_a_mask" not in visitor
            or visitor["wearing_a_mask"] is False
        ):
            raise NotWearingMaskError("Visitor not wearing mask")
        return f"Welcome to {self.name}"
