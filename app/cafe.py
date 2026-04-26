import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("No vaccine")

        today = datetime.date.today()
        expiration_date = visitor["vaccine"]["expiration_date"]

        if expiration_date < today:
            raise OutdatedVaccineError("Vaccine expired")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("No mask")
        return f"Welcome to {self.name}"
