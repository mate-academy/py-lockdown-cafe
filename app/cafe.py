from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)  # Correct import


class Cafe:
    def __init__(self, name: str) -> None:

        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError()

        vaccine_expiration = visitor["vaccine"]["expiration_date"]
        if vaccine_expiration < date.today():
            raise OutdatedVaccineError()

        if "wearing_a_mask" not in visitor or not visitor["wearing_a_mask"]:
            raise NotWearingMaskError()

        return f"Welcome to {self.name}"
