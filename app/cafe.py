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
            raise NotVaccinatedError("You need a vaccine.")
        expiration_date = visitor["vaccine"]["expiration_date"]
        current_date = datetime.date.today()

        if not expiration_date >= current_date:
            raise OutdatedVaccineError("You need valid vaccine.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You must wear a mask.")
        return f"Welcome to {self.name}"
