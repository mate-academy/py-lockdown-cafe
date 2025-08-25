from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError)
from typing import Any
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Any:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("No vaccinated person")
        else:
            today = datetime.date.today()
            expiration_date = visitor["vaccine"]["expiration_date"]
            if today > expiration_date:
                raise OutdatedVaccineError("Visitor's vaccine is expired")

        if ("wearing_a_mask" not in visitor.keys()
                or visitor["wearing_a_mask"] is False):
            raise NotWearingMaskError("Visitor must wear a mask")
        return f"Welcome to {self.name}"
