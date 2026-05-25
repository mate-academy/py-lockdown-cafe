import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor needs to be vaccinated!")

        expiration = visitor["vaccine"]["expiration_date"]
        if expiration < datetime.date.today():
            raise OutdatedVaccineError("The guest has outdated vaccine!")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("The guest is not wearing a mask!")

        return f"Welcome to {self.name}"
