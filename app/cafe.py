from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
from datetime import date
from typing import Any


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Any:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor does not have vaccine")
        elif visitor["vaccine"].get("expiration_date") < date.today():
            raise OutdatedVaccineError("Visitor has an outdated vaccine")
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor does not wearing mask")
        else:
            return f"Welcome to {self.name}"
