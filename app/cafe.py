import datetime

from app.errors import (
    OutdatedVaccineError,
    NotVaccinatedError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Person must be vaccinated to visit cafe")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Expired vaccine, need current")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Masks required for cafe entry")

        return f"Welcome to {self.name}"
