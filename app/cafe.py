import datetime

from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(
                f"{visitor['name']} is not vaccinated!")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor['name']} vaccine is outdated!")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                f"{visitor['name']} is not wearing mask!")
        return f"Welcome to {self.name}"
