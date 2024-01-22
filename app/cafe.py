from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
from datetime import date


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")
        elif visitor.get("vaccine").get("expiration_date") < date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")
        elif visitor.get("wearing_a_mask") is not True:
            raise NotWearingMaskError("NotWearingMaskError")
        else:
            return f"Welcome to {self.name}"
