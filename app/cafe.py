from datetime import date

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor don't have the vaccine.")
        if "expiration_date" in visitor["vaccine"]:
            expiration_date = visitor["vaccine"]["expiration_date"]
            if expiration_date < date.today():
                raise OutdatedVaccineError("Visitor's vaccine is outdated.")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor don't have the mask.")
        return f"Welcome to {self.name}"
