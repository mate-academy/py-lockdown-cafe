from datetime import date

from app.errors import (NotWearingMaskError,
                        OutdatedVaccineError,
                        NotVaccinatedError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("visitor haven't vaccine")
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("visitor have outdated vaccine")
        elif visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("visitor haven't mask")
        return f"Welcome to {self.name}"
