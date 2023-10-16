from datetime import date
from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Not vaccinated")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < date.today():
            raise OutdatedVaccineError("Outdated vaccine")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Not wearing a mask")

        return f"Welcome to {self.name}"
