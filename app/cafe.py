import datetime
from typing import Dict

import app.errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict) -> str:
        if "vaccine" not in visitor:
            raise app.errors.NotVaccinatedError()
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise app.errors.OutdatedVaccineError()
        elif not visitor.get("wearing_a_mask", False):
            raise app.errors.NotWearingMaskError()
        else:
            return f"Welcome to {self.name}"
