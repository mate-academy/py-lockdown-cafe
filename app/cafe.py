from datetime import date
from app.errors import (NotVaccinatedError, OutdatedVaccineError,
                        NotWearingMaskError)
from typing import Dict, Any


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict[str, Any]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError()

        if "vaccine" in visitor:
            expiration_date = visitor["vaccine"]["expiration_date"]
            if expiration_date < date.today():
                raise OutdatedVaccineError()

        if "wearing_a_mask" not in visitor or not visitor["wearing_a_mask"]:
            raise NotWearingMaskError()

        return f"Welcome to {self.name}"
