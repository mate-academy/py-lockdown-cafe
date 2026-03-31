from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine", None):
            raise NotVaccinatedError("Is not vaccinated")
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Vaccine certificate is not valid")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Customer does not have mask")
        return f"Welcome to {self.name}"
