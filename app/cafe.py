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
            raise NotVaccinatedError(f'{visitor["name"]} is not vaccinated.')
        if ("expiration_date" not in visitor["vaccine"]
                or visitor["vaccine"]["expiration_date"]
                < datetime.date.today()):
            raise OutdatedVaccineError(
                f'{visitor["name"]}\'s vaccine is outdated.')
        if ("wearing_a_mask" not in visitor
                or not visitor["wearing_a_mask"]):
            raise NotWearingMaskError(
                f'{visitor["name"]} is not wearing a mask.')
        return f"Welcome to {self.name}"
