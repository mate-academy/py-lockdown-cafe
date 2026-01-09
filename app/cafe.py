import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, friend: dict) -> str:
        if "vaccine" not in friend:
            raise NotVaccinatedError("Person is not vaccinated")

        if friend["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated")

        if not friend.get("wearing_a_mask"):
            raise NotWearingMaskError("Person is not wearing a mask")

        return f"Welcome to {self.name}"
