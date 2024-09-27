import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Guests need a vaccine")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Guests need an unexpired vaccine")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Guests must have a mask")

        return f"Welcome to {self.name}"
