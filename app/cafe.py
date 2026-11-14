import datetime

from app.errors import (OutdatedVaccineError,
                        NotWearingMaskError,
                        NotVaccinatedError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Vaccine is required")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Mask is required")

        return f"Welcome to {self.name}"
