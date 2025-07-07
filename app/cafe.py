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
            raise NotVaccinatedError("You don't have vaccine certificate.")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Your certificate is outdated.")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("You don't wear a mask.")

        return f"Welcome to {self.name}"
