from datetime import date

from app.errors import NotVaccinatedError, OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You need to get a vaccine first.")
        if ("expiration_date" not in visitor["vaccine"]
                or visitor["vaccine"]["expiration_date"] < date.today()):
            raise OutdatedVaccineError("Your vaccine is outdated.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You need to wear a mask.")
        return f"Welcome to {self.name}"
