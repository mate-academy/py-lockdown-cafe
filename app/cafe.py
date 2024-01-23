from datetime import date

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor doesn't have vaccine")
        elif visitor.get("vaccine").get("expiration_date") < date.today():
            raise OutdatedVaccineError("Vaccine is outdated")
        elif visitor.get("wearing_a_mask") is not True:
            raise NotWearingMaskError("Visitor doesn't have a mask")
        return f"Welcome to {self.name}"
