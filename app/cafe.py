from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)

import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor should be vaccinated")

        expiration_date = visitor["vaccine"]["expiration_date"]
        current_date = datetime.date.today()
        if expiration_date < current_date:
            raise OutdatedVaccineError("Visitor should be vaccinated")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor should buy a mask")

        return f"Welcome to {self.name}"
