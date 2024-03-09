from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, human: dict) -> str:
        if "vaccine" not in human:
            raise NotVaccinatedError("NotVaccinatedError")
        if human["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")
        if human["wearing_a_mask"] is False:
            raise NotWearingMaskError("NotWearingMaskError")
        return f"Welcome to {self.name}"
