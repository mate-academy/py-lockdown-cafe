import datetime
from errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("No vaccine found.")

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine expired.")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("No mask.")

        return f"Welcome to {self.name}"
