from datetime import date

from app.errors import (OutdatedVaccineError,
                        NotVaccinatedError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")

        expiration_data = visitor["vaccine"].get("expiration_date")
        if expiration_data is None:
            raise OutdatedVaccineError("OutdatedVaccineError")
        if expiration_data < date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")

        if not visitor.get("wearing_a_mask", True):
            raise NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"
