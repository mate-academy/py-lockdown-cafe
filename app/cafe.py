from datetime import date

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine", False):
            raise NotVaccinatedError("Vaccine is not")
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Vaccine is outdated")
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Wearing mask is not")
        return f"Welcome to {self.name}"
