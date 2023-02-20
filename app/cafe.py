from app.errors import (
    NotVaccinatedError, OutdatedVaccineError,
    NotWearingMaskError
)
from datetime import date


class Cafe:
    def __init__(self, name: str) -> str:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" in visitor:
            expiration_date = visitor["vaccine"]["expiration_date"]
            if expiration_date < date.today():
                raise OutdatedVaccineError("Vaccine has expired.")
            elif visitor["wearing_a_mask"] is False:
                raise NotWearingMaskError(
                    "NotWearingMaskError shouldn't inherit VaccineError class"
                )
            elif visitor["wearing_a_mask"]:
                return f"Welcome to {self.name}"
        elif "vaccine" not in visitor:
            raise NotVaccinatedError(
                "NotVaccinatedError should be raised with a message"
            )
