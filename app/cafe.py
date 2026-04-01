from datetime import date

from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor don't have a vaccine")
        if date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("Vaccine is outdated")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Mask should wearing")

        return f"Welcome to {self.name}"
