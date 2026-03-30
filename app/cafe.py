from typing import Dict
from datetime import date

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError
                        )


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor should have vaccine.")
        if date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("The vaccination has expired.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor should have mask")
        return f"Welcome to {self.name}"
