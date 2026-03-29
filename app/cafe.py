from typing import Any
from app.errors import (
    OutdatedVaccineError,
    NotVaccinatedError,
    NotWearingMaskError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Any:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("All friends should be vaccinated")
        elif (
            visitor["vaccine"].get("expiration_date")
            < datetime.date.today()
        ):
            raise OutdatedVaccineError("All friends should be vaccinated")
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Friends should buy some masks")
        return f"Welcome to {self.name}"
