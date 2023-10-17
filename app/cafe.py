from datetime import date

from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You must be vaccinate")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Your vaccine is outdated")
        if ("wearing_a_mask" not in visitor
                or visitor["wearing_a_mask"] is False):
            raise NotWearingMaskError("Buy a mask")
        return f"Welcome to {self.name}"
