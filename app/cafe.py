import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Client have to be vaccinated")
        elif datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("Vaccine shouldn't be expired")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Client have to wear a mask")
        return f"Welcome to {self.name}"
