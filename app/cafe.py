from datetime import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All friends should be vaccinated")
        elif datetime.now().date() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("All friends should be vaccinated")
        elif not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Friends should buy masks")

        return f"Welcome to {self.name}"
