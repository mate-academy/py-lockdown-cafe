from app.errors import (
    NotWearingMaskError, NotVaccinatedError,
    OutdatedVaccineError
)
from datetime import date


class Cafe:
    def __init__(self, name: str) -> str:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "NotVaccinatedError should be raised with a message"
            )

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < date.today():
            raise OutdatedVaccineError("Vaccine has expired.")

        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        else:
            return f"Welcome to {self.name}"
