import datetime
from typing import Any
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Any:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor should be vaccinated")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor should be vaccinated")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Should buy a mask")
        return f"Welcome to {self.name}"
