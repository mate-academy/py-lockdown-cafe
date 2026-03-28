from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor doesn't have a vaccine")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Vaccine is outdated.")
        if "wearing_a_mask" not in visitor or visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor is not wearing a mask.")
        return f"Welcome to {self.name}"
